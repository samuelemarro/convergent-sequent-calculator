# Generated from SequentCalculus.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SequentCalculusParser import SequentCalculusParser
else:
    from SequentCalculusParser import SequentCalculusParser

# This class defines a complete generic visitor for a parse tree produced by SequentCalculusParser.

class SequentCalculusVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SequentCalculusParser#multiset.
    def visitMultiset(self, ctx:SequentCalculusParser.MultisetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SequentCalculusParser#labelledFormula.
    def visitLabelledFormula(self, ctx:SequentCalculusParser.LabelledFormulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SequentCalculusParser#atom.
    def visitAtom(self, ctx:SequentCalculusParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SequentCalculusParser#statement.
    def visitStatement(self, ctx:SequentCalculusParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SequentCalculusParser#formula.
    def visitFormula(self, ctx:SequentCalculusParser.FormulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SequentCalculusParser#antecedent.
    def visitAntecedent(self, ctx:SequentCalculusParser.AntecedentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SequentCalculusParser#consequent.
    def visitConsequent(self, ctx:SequentCalculusParser.ConsequentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SequentCalculusParser#sequent.
    def visitSequent(self, ctx:SequentCalculusParser.SequentContext):
        return self.visitChildren(ctx)



del SequentCalculusParser