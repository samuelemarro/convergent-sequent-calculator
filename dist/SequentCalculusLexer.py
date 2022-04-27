# Generated from SequentCalculus.g4 by ANTLR 4.10.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,17,77,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,
        7,13,2,14,7,14,2,15,7,15,2,16,7,16,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,
        3,1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,7,1,8,1,8,1,9,1,9,1,10,1,10,
        1,11,1,11,1,12,1,12,1,13,1,13,1,14,1,14,1,15,4,15,68,8,15,11,15,
        12,15,69,1,15,1,15,1,16,1,16,1,16,1,16,0,0,17,1,1,3,2,5,3,7,4,9,
        5,11,6,13,7,15,8,17,9,19,10,21,11,23,12,25,13,27,14,29,15,31,16,
        33,17,1,0,3,1,0,97,122,2,0,65,90,124,124,2,0,10,10,13,13,77,0,1,
        1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,
        0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,
        0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,
        0,0,0,33,1,0,0,0,1,35,1,0,0,0,3,37,1,0,0,0,5,39,1,0,0,0,7,41,1,0,
        0,0,9,43,1,0,0,0,11,45,1,0,0,0,13,47,1,0,0,0,15,49,1,0,0,0,17,52,
        1,0,0,0,19,54,1,0,0,0,21,56,1,0,0,0,23,58,1,0,0,0,25,60,1,0,0,0,
        27,62,1,0,0,0,29,64,1,0,0,0,31,67,1,0,0,0,33,73,1,0,0,0,35,36,5,
        44,0,0,36,2,1,0,0,0,37,38,5,58,0,0,38,4,1,0,0,0,39,40,5,61,0,0,40,
        6,1,0,0,0,41,42,5,38,0,0,42,8,1,0,0,0,43,44,5,124,0,0,44,10,1,0,
        0,0,45,46,5,63,0,0,46,12,1,0,0,0,47,48,5,33,0,0,48,14,1,0,0,0,49,
        50,5,194,0,0,50,51,5,176,0,0,51,16,1,0,0,0,52,53,5,94,0,0,53,18,
        1,0,0,0,54,55,7,0,0,0,55,20,1,0,0,0,56,57,7,1,0,0,57,22,1,0,0,0,
        58,59,5,40,0,0,59,24,1,0,0,0,60,61,5,41,0,0,61,26,1,0,0,0,62,63,
        5,64,0,0,63,28,1,0,0,0,64,65,5,46,0,0,65,30,1,0,0,0,66,68,5,32,0,
        0,67,66,1,0,0,0,68,69,1,0,0,0,69,67,1,0,0,0,69,70,1,0,0,0,70,71,
        1,0,0,0,71,72,6,15,0,0,72,32,1,0,0,0,73,74,7,2,0,0,74,75,1,0,0,0,
        75,76,6,16,0,0,76,34,1,0,0,0,2,0,69,1,6,0,0
    ]

class SequentCalculusLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    ARROW = 3
    AND = 4
    OR = 5
    IMPLIES = 6
    NOT = 7
    BOX = 8
    DIAMOND = 9
    LABEL = 10
    VARIABLE = 11
    LPAREN = 12
    RPAREN = 13
    BOT = 14
    RELATION = 15
    WS = 16
    SKIPPABLE = 17

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "','", "':'", "'='", "'&'", "'|'", "'?'", "'!'", "'\\u00C2\\u00B0'", 
            "'^'", "'('", "')'", "'@'", "'.'" ]

    symbolicNames = [ "<INVALID>",
            "ARROW", "AND", "OR", "IMPLIES", "NOT", "BOX", "DIAMOND", "LABEL", 
            "VARIABLE", "LPAREN", "RPAREN", "BOT", "RELATION", "WS", "SKIPPABLE" ]

    ruleNames = [ "T__0", "T__1", "ARROW", "AND", "OR", "IMPLIES", "NOT", 
                  "BOX", "DIAMOND", "LABEL", "VARIABLE", "LPAREN", "RPAREN", 
                  "BOT", "RELATION", "WS", "SKIPPABLE" ]

    grammarFileName = "SequentCalculus.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


