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
        return set(re.findall(r'\b[A-Z]\b', self.content))

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
        ('^', ' ◇ ')
    ]

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Formula):
            return self.content == other.content
    
    def __hash__(self) -> int:
        return hash(self.content)

class LabelledFormula:
    def __init__(self, label : str, formula : Union[Formula, str]) -> None:
        self.label = label

        if isinstance(formula, str):
            formula = Formula(formula)

        self.formula = formula
    
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

class Sequent:
    def __init__(self, antecedents : Union[List[LabelledFormula], Set[LabelledFormula]], consequents : Union[List[LabelledFormula], Set[LabelledFormula]]) -> None:
        if isinstance(antecedents, list):
            antecedents = set(antecedents)
        
        if isinstance(consequents, list):
            consequents = set(consequents)

        self.antecedents = antecedents
        self.consequents = consequents

    def labels(self):
        return set([f.label for f in self.antecedents]) | set([f.label for f in self.consequents])

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
