import re

from typing import List, Set, Union


"""class Rule:
    def name(self):
        return 'Unnamed rule'

    def nAntecedents(self):
        raise NotImplementedError

    def nConsequents(self):
        raise NotImplementedError

    def apply(self, node: Node):
        raise NotImplementedError

    def __call__(self, node: Node):
        return self.apply(node)

class LAndRule(Rule):
    def name(self):
        return 'L/\\'
    

    def apply(self, node: Node):"""

class Formula:
    def __init__(self, content : str) -> None:
        self.content = content

    def prop_variables(self) -> Set[str]:
        return set(re.findall(r'\b[A-P|Q-Z]\b', self.content))

    def semantic_variables(self) -> Set[str]:
        return set(re.findall(r'\b[a-z]\b', self.content))
    
    def replace_prop_variable(self, old, new) -> 'Formula':
        return Formula(self.content.replace(old, new))

    def replace_semantic_variable(self, old, new) -> 'Formula':
        return Formula(self.content.replace(old, new))
    
    def clone(self) -> 'Formula':
        return Formula(self.content)
    
    def __str__(self) -> str:
        formatted = self.content

        for old, new in self.REPLACEMENTS:
            formatted = formatted.replace(old, new)
        return formatted
    
    __repr__ = __str__

    REPLACEMENTS = [
        ('&', ' ∧ '),
        ('|', ' ∨ '),
        ('!', ' ¬ '),
        ('?', ' → '),
        ('°', ' ◻ '),
        ('^', ' ◇ '),
        ('@', '⊥'),
    ]

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Formula):
            return self.content == other.content
    
    def __hash__(self) -> int:
        return hash(self.content)

# Superclass for both atoms and labelled formulas
class Statement:
    def prop_variables(self) -> Set[str]:
        raise NotImplementedError
    
    def semantic_variables(self) -> Set[str]:
        raise NotImplementedError
    
    def replace_prop_variable(self, old, new) -> 'Statement':
        raise NotImplementedError

    def replace_semantic_variable(self, old, new) -> 'Statement':
        raise NotImplementedError

    def replace_label(self, old, new) -> 'Statement':
        raise NotImplementedError

    def clone(self) -> 'Statement':
        raise NotImplementedError

class LabelledFormula(Statement):
    def __init__(self, label : str, formula : Union[Formula, str]) -> None:
        self.label = label

        if isinstance(formula, str):
            formula = Formula(formula)

        self.formula = formula
    
    def labels(self) -> Set[str]:
        return set([self.label])
    
    def prop_variables(self) -> Set[str]:
        return self.formula.prop_variables()
    
    def semantic_variables(self) -> Set[str]:
        return self.formula.semantic_variables()
    
    def replace_prop_variable(self, old, new) -> 'LabelledFormula':
        return LabelledFormula(self.label, self.formula.replace_prop_variable(old, new))

    def replace_semantic_variable(self, old, new) -> 'LabelledFormula':
        return LabelledFormula(self.label, self.formula.replace_semantic_variable(old, new))

    def replace_label(self, old, new) -> 'LabelledFormula':
        if self.label == old:
            new_label = new
        else:
            new_label = self.label
        return LabelledFormula(new_label, self.formula)

    def clone(self) -> 'LabelledFormula':
        return LabelledFormula(self.label, self.formula.clone())
    
    def __str__(self) -> str:
        return self.label + ':' + str(self.formula)
    
    __repr__ = __str__

    def __eq__(self, other) -> bool:
        if isinstance(other, LabelledFormula):
            return self.label == other.label and self.formula == other.formula
        return False
    
    def __hash__(self) -> int:
        return hash(self.label) + hash(self.formula)

class Atom(Statement):
    def __init__(self, label1, label2) -> None:
        self.label1 = label1
        self.label2 = label2

    def labels(self) -> Set[str]:
        return set([self.label1, self.label2])

    def prop_variables(self) -> Set[str]:
        return set()
    
    def semantic_variables(self) -> Set[str]:
        return set()
    
    def replace_prop_variable(self, old, new) -> 'Atom':
        return self.clone()

    def replace_semantic_variable(self, old, new) -> 'Atom':
        return self.clone()

    def replace_label(self, old, new) -> 'Atom':
        if self.label1 == old:
            new_label1 = new
        else:
            new_label1 = self.label1

        if self.label2 == old:
            new_label2 = new
        else:
            new_label2 = self.label2

        return Atom(new_label1, new_label2)

    def clone(self) -> 'Atom':
        return Atom(self.label1, self.label2)
    
    def __str__(self) -> str:
        return self.label1 + 'R' + self.label2
    
    __repr__ = __str__

    def __eq__(self, other) -> bool:
        if isinstance(other, Atom):
            return self.label1 == other.label1 and self.label2 == other.label2
        return False
    
    def __hash__(self) -> int:
        return hash(self.label1) + hash(self.label2)

class Sequent:
    def __init__(self, antecedents : Union[List[Statement], Set[Statement]], consequents : Union[List[Statement], Set[Statement]]) -> None:
        if isinstance(antecedents, list) or isinstance(antecedents, tuple):
            antecedents = set(antecedents)
        
        if isinstance(consequents, list) or isinstance(consequents, tuple):
            consequents = set(consequents)

        self.antecedents = antecedents
        self.consequents = consequents

    def labels(self):
        all_labels = set()
        for statement in self.antecedents | self.consequents:
            all_labels |= statement.labels()
        return all_labels

    def prop_variables(self):
        all_variables = set()

        for antecedent in self.antecedents:
            all_variables |= antecedent.prop_variables()
        
        for consequent in self.consequents:
            all_variables |= consequent.prop_variables()
        
        return all_variables

    def semantic_variables(self):
        all_variables = set()

        for antecedent in self.antecedents:
            all_variables |= antecedent.semantic_variables()
        
        for consequent in self.consequents:
            all_variables |= consequent.semantic_variables()
        
        return all_variables
    
    def replace_prop_variable(self, old : str, new : str) -> 'Sequent':
        new_antecedents = [antecedent.replace_prop_variable(old, new) for antecedent in self.antecedents]
        new_consequents = [consequent.replace_prop_variable(old, new) for consequent in self.consequents]
        return Sequent(new_antecedents, new_consequents)

    def replace_semantic_variable(self, old : str, new : str) -> 'Sequent':
        new_antecedents = [antecedent.replace_semantic_variable(old, new) for antecedent in self.antecedents]
        new_consequents = [consequent.replace_semantic_variable(old, new) for consequent in self.consequents]
        return Sequent(new_antecedents, new_consequents)

    def replace_label(self, old : str, new : str) -> 'Sequent':
        new_antecedents = [antecedent.replace_label(old, new) for antecedent in self.antecedents]
        new_consequents = [consequent.replace_label(old, new) for consequent in self.consequents]
        return Sequent(new_antecedents, new_consequents)

    def clone(self) -> 'Sequent':
        new_antecedents = [antecedent.clone() for antecedent in self.antecedents]
        new_consequents = [consequent.clone() for consequent in self.consequents]
        return Sequent(new_antecedents, new_consequents)

    def __str__(self) -> str:
        return ','.join([str(antecedent) for antecedent in self.antecedents]) + ' ⇒  ' + ','.join([str(consequent) for consequent in self.consequents])
    
    __repr__ = __str__

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Sequent):
            return self.antecedents == other.antecedents and self.consequents == other.consequents
        return False
