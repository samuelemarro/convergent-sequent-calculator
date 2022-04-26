import re

from typing import List
from antlr4 import CommonTokenStream, ParseTreeWalker, StdinStream, InputStream, ParserRuleContext
from antlr4.tree.Tree import TerminalNodeImpl

from dist.SequentCalculusLexer import SequentCalculusLexer

#import click
from dist.SequentCalculusParser import SequentCalculusParser
from dist.SequentCalculusListener import SequentCalculusListener

from base import Sequent, LabelledFormula, Formula
from rule import Rule
import parsing


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


def traverse(tree, rule_names, indent = 0):
    if tree.getText() == "<EOF>":
        return
    elif isinstance(tree, TerminalNodeImpl):
        print("{0}TOKEN='{1}'".format("  " * indent, tree.getText()))
    else:
        print("{0}{1}".format("  " * indent, rule_names[tree.getRuleIndex()]))
        for child in tree.children:
            traverse(child, rule_names, indent + 1)   

def parse_tree(tree, rule_names):
    if tree.getText() == '<EOF>':
        return None
    elif isinstance(tree, TerminalNodeImpl):
        return tree.getText()
    else:
        parsed_children = []
        for child in tree.children:
            parsed_child = parse_tree(child, rule_names)
            parsed_children.append(parsed_child)

        return {
            'rule' : rule_names[tree.getRuleIndex()],
            'children' : parsed_children
        }

def parse_tree_2(tree, rule_names):
    if tree.getText() == '<EOF>':
        return None
    elif isinstance(tree, TerminalNodeImpl):
        return tree.getText()
    else:
        parsed_children = []
        for child in tree.children:
            parsed_child = parse_tree(child, rule_names)
            parsed_children.append(parsed_child)

        return {
            'rule' : rule_names[tree.getRuleIndex()],
            'children' : parsed_children
        }


def preprocess(_input):
    replacements = [
        ('AND', '&'),
        ('/\\', '&'),
        ('OR', '|'),
        ('\\/', '|'),
        ('NOT', '!'),
        ('-', '!'),
        ('~', '!'),
        ('IMPLIES', '?'),
        ('->', '?'),
        ('BOX', '°'),
        ('[]', '°'),
        ('DIAMOND', '^'),
        ('<>', '^'),
        ('=>', '=')
    ]

    for old, new in replacements:
        _input = _input.replace(old, new)
    _input = re.sub('\s+', '', _input)

    return _input

def main():
    _input = 'w:(A AND B)=>w:A'

    _input = preprocess(_input)

    print(_input)

    lexer = SequentCalculusLexer(InputStream(_input))
    stream = CommonTokenStream(lexer)
    parser = SequentCalculusParser(stream)

    tree = parser.sequent()

    traverse(tree, parser.ruleNames)

    print(parse_tree(tree, parser.ruleNames))

    #traverse(tree, parser.ruleNames)
    printer = TreeConverter()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)

    sequent = Sequent(printer.antecedents, printer.consequents)

    rule = Rule('LAnd', 
        Sequent([LabelledFormula('w', preprocess('(A AND B)'))], [LabelledFormula('w', 'A')]),
        []
    )
    print('Prop variables:', rule.root.prop_variables())
    print('Semantic variables:', rule.root.semantic_variables())
    print('Labels:', rule.root.labels())
    print(parsing.get_immediate_children(Formula(preprocess('(A AND (B AND C))')), parser.ruleNames))

    rule.apply_to_relevant_sequent(sequent, parser.ruleNames)

    print(sequent)

if __name__ == '__main__':
    main()