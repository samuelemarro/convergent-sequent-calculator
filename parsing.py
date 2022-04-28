import re

from antlr4 import CommonTokenStream, InputStream, ParseTreeWalker

from base import Atom, Formula, LabelledFormula, Sequent

from dist.SequentCalculusLexer import SequentCalculusLexer

#import click
from dist.SequentCalculusParser import SequentCalculusParser
from dist.SequentCalculusListener import SequentCalculusListener

REPLACEMENTS = [
    ('AND', '&'),
    ('/\\', '&'),
    ('OR', '|'),
    ('\\/', '|'),
    ('~', '!'),
    ('IMPLIES', '?'),
    ('->', '?'),
    ('NOT', '!'),
    ('-', '!'),
    ('BOX', '#'),
    ('[]', '#'),
    ('DIAMOND', '^'),
    ('<>', '^'),
    ('=>', '='),
    ('BOT', '@'),
    ('+', '@'),
    ('R', '.'),
    ('SEES', '.'),
]


SKIPPABLE_CHILDREN = set([p[1] for p in REPLACEMENTS]) | set(['(', ')'])

def get_immediate_children_set(formula : Formula, skip_children : set = SKIPPABLE_CHILDREN):
    lexer = SequentCalculusLexer(InputStream(formula.content))
    stream = CommonTokenStream(lexer)
    parser = SequentCalculusParser(stream)

    tree = parser.formula()

    #while rule_names[tree.getRuleIndex()] != 'inner_formula':
    #    valid_children = [child for child in tree.getChildren() if not isinstance(child, TerminalNodeImpl)]
    #    assert len(valid_children) == 1
    #    tree = valid_children[0]

    while tree.children[0].getText() == '(':
        tree = tree.children[1]

    immediate_children = dict()

    for child in tree.children:
        child_text = child.getText()
        if child_text not in immediate_children:
            immediate_children[child_text] = []

        start, stop = child.getSourceInterval()
        
        immediate_children[child_text].append((start, stop))
    
    return [child for child in immediate_children if child not in SKIPPABLE_CHILDREN]

def get_immediate_children_list(formula : Formula):
    lexer = SequentCalculusLexer(InputStream(formula.content))
    stream = CommonTokenStream(lexer)
    parser = SequentCalculusParser(stream)

    tree = parser.formula()

    return [child.getText() for child in tree.children]

def preprocess(_input):
    for old, new in REPLACEMENTS:
        _input = _input.replace(old, new)
    _input = re.sub('\s+', '', _input)

    return _input

class TreeConverter(SequentCalculusListener):
    def __init__(self):
        self.is_antecedent = True
        self.antecedents = []
        self.consequents = []

    def exitAntecedent(self, ctx: SequentCalculusParser.AntecedentContext):
        self.is_antecedent = False
    
    def enterFormula(self, ctx: SequentCalculusParser.FormulaContext):
        return super().enterFormula(ctx)

    def enterLabelledFormula(self, ctx):
        label = ctx.getChild(0).symbol.text
        formula_text = ctx.getChild(2).getText()

        labelled_formula = LabelledFormula(label, Formula(formula_text))
    
        if self.is_antecedent:
            self.antecedents.append(labelled_formula)
        else:
            self.consequents.append(labelled_formula)
    
    def enterAtom(self, ctx: SequentCalculusParser.AtomContext):
        label1 = ctx.getChild(0).symbol.text
        label2 = ctx.getChild(2).symbol.text

        atom = Atom(label1, label2)

        if self.is_antecedent:
            self.antecedents.append(atom)
        else:
            self.consequents.append(atom)

def parse_sequent(sequent_text : str):
    sequent_text = preprocess(sequent_text)

    lexer = SequentCalculusLexer(InputStream(sequent_text))
    stream = CommonTokenStream(lexer)
    parser = SequentCalculusParser(stream)

    tree = parser.sequent()
    printer = TreeConverter()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)

    sequent = Sequent(printer.antecedents, printer.consequents)

    return sequent