from typing import List

from antlr4 import CommonTokenStream, ParseTreeWalker, StdinStream, InputStream
from antlr4.tree.Tree import TerminalNodeImpl
from base import Formula

from dist.SequentCalculusLexer import SequentCalculusLexer

#import click
from dist.SequentCalculusParser import SequentCalculusParser
from dist.SequentCalculusListener import SequentCalculusListener

SKIPPABLE_CHILDREN = ['(', ')', '&', '|', '^', '°']

def get_immediate_children(formula : Formula, rule_names : List[str]):
    lexer = SequentCalculusLexer(InputStream(formula.content))
    stream = CommonTokenStream(lexer)
    parser = SequentCalculusParser(stream)

    tree = parser.formula()

    #while rule_names[tree.getRuleIndex()] != 'inner_formula':
    #    valid_children = [child for child in tree.getChildren() if not isinstance(child, TerminalNodeImpl)]
    #    assert len(valid_children) == 1
    #    tree = valid_children[0]

    immediate_children = dict()

    for child in tree.children:
        child_text = child.getText()
        if child_text not in immediate_children:
            immediate_children[child_text] = []

        start, stop = child.getSourceInterval()
        
        immediate_children[child_text].append((start, stop))
    
    return [child for child in immediate_children if child not in SKIPPABLE_CHILDREN]