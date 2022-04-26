import re
from typing import Dict, List, Tuple

from base import Formula, LabelledFormula, Sequent
import parsing
import utils

def replace_formula_children(formula : Formula, start : int, end : int, replacement : str):
    new_formula_content = formula.content[:start] + replacement + formula.content[end:]
    
    return Formula(new_formula_content)

def replace_labelled_formula_children(labelled_formula : LabelledFormula, start : int, end : int, replacement : str):
    return LabelledFormula(labelled_formula.label, replace_formula_children(labelled_formula.formula, start, end, replacement))

def replace_sequent_children(sequent : Sequent, multiset: str, index : int, start : int, end : int, replacement : str):
    new_antecedents = [antecedent.clone() for antecedent in sequent.antecedents]
    new_consequents = [consequent.clone() for consequent in sequent.consequents]

    if multiset == 'antecedent':
        new_antecedents[index] = replace_labelled_formula_children(new_antecedents[index], start, end, replacement)
    else:
        new_consequents[index] = replace_labelled_formula_children(new_consequents[index], start, end, replacement)
    
    return Sequent(new_antecedents, new_consequents)

def get_labelled_formula_immediate_children(labelled_formula : LabelledFormula, rule_names: List[str]):
    return parsing.get_immediate_children(labelled_formula.formula, rule_names)

def get_sequent_immediate_children(sequent : Sequent, rule_names):
    # Merge the immediate children
    immediate_children = {}
    
    for index, antecedent in enumerate(sequent.antecedents):
        antecedent_immediate_children = get_labelled_formula_immediate_children(antecedent, rule_names)

        for immediate_child_text, immediate_child_positions in antecedent_immediate_children.items():
            if immediate_child_text not in immediate_children:
                immediate_children[immediate_child_text] = []
            for start, stop in immediate_child_positions:
                immediate_children[immediate_child_text].append(('antecedent', index, start, stop))
    
    for index, consequent in enumerate(sequent.consequent):
        consequent_immediate_children = get_labelled_formula_immediate_children(consequent, rule_names)

        for immediate_child_text, immediate_child_positions in consequent_immediate_children.items():
            if immediate_child_text not in immediate_children:
                immediate_children[immediate_child_text] = []
            for start, stop in immediate_child_positions:
                immediate_children[immediate_child_text].append(('consequent', index, start, stop))

    return immediate_children

class Rule:
    def __init__(self, name, root : Sequent, children : List[Sequent]):
        self.name = name
        self.root = root
        self.children = children

    def apply_to_relevant_sequent(self, relevant_sequent : Sequent, rule_names):
        known_labels = relevant_sequent.labels()
        known_immediate_children = get_sequent_immediate_children(relevant_sequent, rule_names)
        known_semantic_variables = relevant_sequent.semantic_variables()

        unknown_labels = self.root.labels()
        unknown_prop_variables = self.root.prop_variables()
        unknown_semantic_variables = self.root.semantic_variables()

        # Match unknown with known
        label_pairings = utils.get_pairings(unknown_labels, known_labels)
        prop_variable_pairings = utils.get_pairings(unknown_prop_variables, known_immediate_children.keys())
        semantic_variable_pairings = utils.get_pairings(unknown_semantic_variables, known_semantic_variables)

        for label_pairing in label_pairings:
            for prop_variable_pairing in prop_variable_pairings:
                for semantic_variable_pairing in semantic_variable_pairings:
                    adapted_root = self.root.clone()
                    adapted_children = [child.clone() for child in self.children]

                    for old_label, new_label in label_pairing:
                        adapted_root = adapted_root.replace_label(old_label, new_label)
                        adapted_children = [child.replace_label(old_label, new_label) for child in adapted_children]

                    for old_prop_variable, new_immediate_child in prop_variable_pairing:
                        adapted_root = adapted_root.replace_prop_variable(old_prop_variable, new_immediate_child)
                        adapted_children = [child.replace_prop_variable(old_prop_variable, new_immediate_child) for child in adapted_children]
                    
                    for old_semantic_variable, new_semantic_variable in semantic_variable_pairing:
                        adapted_root = adapted_root.replace_semantic_variable(old_semantic_variable, new_semantic_variable)
                        adapted_children = [child.replace_semantic_variable(old_semantic_variable, new_semantic_variable) for child in adapted_children]
                    print(adapted_root)
                    print(adapted_children)