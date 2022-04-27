# Generated from SequentCalculus.g4 by ANTLR 4.10.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,17,81,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,1,0,1,0,1,0,1,0,3,0,22,8,0,1,1,1,1,1,1,1,1,1,2,1,2,
        1,2,1,2,1,3,1,3,3,3,34,8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,3,4,49,8,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,5,4,
        60,8,4,10,4,12,4,63,9,4,1,5,1,5,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,
        1,7,1,7,1,7,1,7,3,7,79,8,7,1,7,0,1,8,8,0,2,4,6,8,10,12,14,0,0,85,
        0,21,1,0,0,0,2,23,1,0,0,0,4,27,1,0,0,0,6,33,1,0,0,0,8,48,1,0,0,0,
        10,64,1,0,0,0,12,66,1,0,0,0,14,78,1,0,0,0,16,17,3,6,3,0,17,18,5,
        1,0,0,18,19,3,0,0,0,19,22,1,0,0,0,20,22,3,6,3,0,21,16,1,0,0,0,21,
        20,1,0,0,0,22,1,1,0,0,0,23,24,5,10,0,0,24,25,5,2,0,0,25,26,3,8,4,
        0,26,3,1,0,0,0,27,28,5,10,0,0,28,29,5,15,0,0,29,30,5,10,0,0,30,5,
        1,0,0,0,31,34,3,2,1,0,32,34,3,4,2,0,33,31,1,0,0,0,33,32,1,0,0,0,
        34,7,1,0,0,0,35,36,6,4,-1,0,36,37,5,12,0,0,37,38,3,8,4,0,38,39,5,
        13,0,0,39,49,1,0,0,0,40,41,5,8,0,0,41,49,3,8,4,8,42,43,5,9,0,0,43,
        49,3,8,4,7,44,45,5,7,0,0,45,49,3,8,4,6,46,49,5,11,0,0,47,49,5,14,
        0,0,48,35,1,0,0,0,48,40,1,0,0,0,48,42,1,0,0,0,48,44,1,0,0,0,48,46,
        1,0,0,0,48,47,1,0,0,0,49,61,1,0,0,0,50,51,10,5,0,0,51,52,5,4,0,0,
        52,60,3,8,4,5,53,54,10,4,0,0,54,55,5,5,0,0,55,60,3,8,4,4,56,57,10,
        3,0,0,57,58,5,6,0,0,58,60,3,8,4,3,59,50,1,0,0,0,59,53,1,0,0,0,59,
        56,1,0,0,0,60,63,1,0,0,0,61,59,1,0,0,0,61,62,1,0,0,0,62,9,1,0,0,
        0,63,61,1,0,0,0,64,65,3,0,0,0,65,11,1,0,0,0,66,67,3,0,0,0,67,13,
        1,0,0,0,68,79,5,3,0,0,69,70,3,10,5,0,70,71,5,3,0,0,71,79,1,0,0,0,
        72,73,5,3,0,0,73,79,3,12,6,0,74,75,3,10,5,0,75,76,5,3,0,0,76,77,
        3,12,6,0,77,79,1,0,0,0,78,68,1,0,0,0,78,69,1,0,0,0,78,72,1,0,0,0,
        78,74,1,0,0,0,79,15,1,0,0,0,6,21,33,48,59,61,78
    ]

class SequentCalculusParser ( Parser ):

    grammarFileName = "SequentCalculus.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "','", "':'", "'='", "'&'", "'|'", "'?'", 
                     "'!'", "'\\u00C2\\u00B0'", "'^'", "<INVALID>", "<INVALID>", 
                     "'('", "')'", "'@'", "'.'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "ARROW", "AND", 
                      "OR", "IMPLIES", "NOT", "BOX", "DIAMOND", "LABEL", 
                      "VARIABLE", "LPAREN", "RPAREN", "BOT", "RELATION", 
                      "WS", "SKIPPABLE" ]

    RULE_multiset = 0
    RULE_labelledFormula = 1
    RULE_atom = 2
    RULE_statement = 3
    RULE_formula = 4
    RULE_antecedent = 5
    RULE_consequent = 6
    RULE_sequent = 7

    ruleNames =  [ "multiset", "labelledFormula", "atom", "statement", "formula", 
                   "antecedent", "consequent", "sequent" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    ARROW=3
    AND=4
    OR=5
    IMPLIES=6
    NOT=7
    BOX=8
    DIAMOND=9
    LABEL=10
    VARIABLE=11
    LPAREN=12
    RPAREN=13
    BOT=14
    RELATION=15
    WS=16
    SKIPPABLE=17

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class MultisetContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(SequentCalculusParser.StatementContext,0)


        def multiset(self):
            return self.getTypedRuleContext(SequentCalculusParser.MultisetContext,0)


        def getRuleIndex(self):
            return SequentCalculusParser.RULE_multiset

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiset" ):
                listener.enterMultiset(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiset" ):
                listener.exitMultiset(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiset" ):
                return visitor.visitMultiset(self)
            else:
                return visitor.visitChildren(self)




    def multiset(self):

        localctx = SequentCalculusParser.MultisetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_multiset)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 16
                self.statement()
                self.state = 17
                self.match(SequentCalculusParser.T__0)
                self.state = 18
                self.multiset()
                pass

            elif la_ == 2:
                self.state = 20
                self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LabelledFormulaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LABEL(self):
            return self.getToken(SequentCalculusParser.LABEL, 0)

        def formula(self):
            return self.getTypedRuleContext(SequentCalculusParser.FormulaContext,0)


        def getRuleIndex(self):
            return SequentCalculusParser.RULE_labelledFormula

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabelledFormula" ):
                listener.enterLabelledFormula(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabelledFormula" ):
                listener.exitLabelledFormula(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLabelledFormula" ):
                return visitor.visitLabelledFormula(self)
            else:
                return visitor.visitChildren(self)




    def labelledFormula(self):

        localctx = SequentCalculusParser.LabelledFormulaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_labelledFormula)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self.match(SequentCalculusParser.LABEL)
            self.state = 24
            self.match(SequentCalculusParser.T__1)
            self.state = 25
            self.formula(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LABEL(self, i:int=None):
            if i is None:
                return self.getTokens(SequentCalculusParser.LABEL)
            else:
                return self.getToken(SequentCalculusParser.LABEL, i)

        def RELATION(self):
            return self.getToken(SequentCalculusParser.RELATION, 0)

        def getRuleIndex(self):
            return SequentCalculusParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = SequentCalculusParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_atom)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.match(SequentCalculusParser.LABEL)
            self.state = 28
            self.match(SequentCalculusParser.RELATION)
            self.state = 29
            self.match(SequentCalculusParser.LABEL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def labelledFormula(self):
            return self.getTypedRuleContext(SequentCalculusParser.LabelledFormulaContext,0)


        def atom(self):
            return self.getTypedRuleContext(SequentCalculusParser.AtomContext,0)


        def getRuleIndex(self):
            return SequentCalculusParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = SequentCalculusParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 31
                self.labelledFormula()
                pass

            elif la_ == 2:
                self.state = 32
                self.atom()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FormulaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(SequentCalculusParser.LPAREN, 0)

        def formula(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SequentCalculusParser.FormulaContext)
            else:
                return self.getTypedRuleContext(SequentCalculusParser.FormulaContext,i)


        def RPAREN(self):
            return self.getToken(SequentCalculusParser.RPAREN, 0)

        def BOX(self):
            return self.getToken(SequentCalculusParser.BOX, 0)

        def DIAMOND(self):
            return self.getToken(SequentCalculusParser.DIAMOND, 0)

        def NOT(self):
            return self.getToken(SequentCalculusParser.NOT, 0)

        def VARIABLE(self):
            return self.getToken(SequentCalculusParser.VARIABLE, 0)

        def BOT(self):
            return self.getToken(SequentCalculusParser.BOT, 0)

        def AND(self):
            return self.getToken(SequentCalculusParser.AND, 0)

        def OR(self):
            return self.getToken(SequentCalculusParser.OR, 0)

        def IMPLIES(self):
            return self.getToken(SequentCalculusParser.IMPLIES, 0)

        def getRuleIndex(self):
            return SequentCalculusParser.RULE_formula

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFormula" ):
                listener.enterFormula(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFormula" ):
                listener.exitFormula(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFormula" ):
                return visitor.visitFormula(self)
            else:
                return visitor.visitChildren(self)



    def formula(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SequentCalculusParser.FormulaContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_formula, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SequentCalculusParser.LPAREN]:
                self.state = 36
                self.match(SequentCalculusParser.LPAREN)
                self.state = 37
                self.formula(0)
                self.state = 38
                self.match(SequentCalculusParser.RPAREN)
                pass
            elif token in [SequentCalculusParser.BOX]:
                self.state = 40
                self.match(SequentCalculusParser.BOX)
                self.state = 41
                self.formula(8)
                pass
            elif token in [SequentCalculusParser.DIAMOND]:
                self.state = 42
                self.match(SequentCalculusParser.DIAMOND)
                self.state = 43
                self.formula(7)
                pass
            elif token in [SequentCalculusParser.NOT]:
                self.state = 44
                self.match(SequentCalculusParser.NOT)
                self.state = 45
                self.formula(6)
                pass
            elif token in [SequentCalculusParser.VARIABLE]:
                self.state = 46
                self.match(SequentCalculusParser.VARIABLE)
                pass
            elif token in [SequentCalculusParser.BOT]:
                self.state = 47
                self.match(SequentCalculusParser.BOT)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 61
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 59
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = SequentCalculusParser.FormulaContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_formula)
                        self.state = 50
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 51
                        self.match(SequentCalculusParser.AND)
                        self.state = 52
                        self.formula(5)
                        pass

                    elif la_ == 2:
                        localctx = SequentCalculusParser.FormulaContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_formula)
                        self.state = 53
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 54
                        self.match(SequentCalculusParser.OR)
                        self.state = 55
                        self.formula(4)
                        pass

                    elif la_ == 3:
                        localctx = SequentCalculusParser.FormulaContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_formula)
                        self.state = 56
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 57
                        self.match(SequentCalculusParser.IMPLIES)
                        self.state = 58
                        self.formula(3)
                        pass

             
                self.state = 63
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AntecedentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiset(self):
            return self.getTypedRuleContext(SequentCalculusParser.MultisetContext,0)


        def getRuleIndex(self):
            return SequentCalculusParser.RULE_antecedent

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAntecedent" ):
                listener.enterAntecedent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAntecedent" ):
                listener.exitAntecedent(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAntecedent" ):
                return visitor.visitAntecedent(self)
            else:
                return visitor.visitChildren(self)




    def antecedent(self):

        localctx = SequentCalculusParser.AntecedentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_antecedent)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.multiset()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConsequentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiset(self):
            return self.getTypedRuleContext(SequentCalculusParser.MultisetContext,0)


        def getRuleIndex(self):
            return SequentCalculusParser.RULE_consequent

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConsequent" ):
                listener.enterConsequent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConsequent" ):
                listener.exitConsequent(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConsequent" ):
                return visitor.visitConsequent(self)
            else:
                return visitor.visitChildren(self)




    def consequent(self):

        localctx = SequentCalculusParser.ConsequentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_consequent)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.multiset()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SequentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARROW(self):
            return self.getToken(SequentCalculusParser.ARROW, 0)

        def antecedent(self):
            return self.getTypedRuleContext(SequentCalculusParser.AntecedentContext,0)


        def consequent(self):
            return self.getTypedRuleContext(SequentCalculusParser.ConsequentContext,0)


        def getRuleIndex(self):
            return SequentCalculusParser.RULE_sequent

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSequent" ):
                listener.enterSequent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSequent" ):
                listener.exitSequent(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSequent" ):
                return visitor.visitSequent(self)
            else:
                return visitor.visitChildren(self)




    def sequent(self):

        localctx = SequentCalculusParser.SequentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_sequent)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 68
                self.match(SequentCalculusParser.ARROW)
                pass

            elif la_ == 2:
                self.state = 69
                self.antecedent()
                self.state = 70
                self.match(SequentCalculusParser.ARROW)
                pass

            elif la_ == 3:
                self.state = 72
                self.match(SequentCalculusParser.ARROW)
                self.state = 73
                self.consequent()
                pass

            elif la_ == 4:
                self.state = 74
                self.antecedent()
                self.state = 75
                self.match(SequentCalculusParser.ARROW)
                self.state = 76
                self.consequent()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[4] = self.formula_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def formula_sempred(self, localctx:FormulaContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         




