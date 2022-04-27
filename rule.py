from typing import Iterable, List, Set, Tuple, Union

from enum import Enum
import string

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
    return parsing.get_immediate_children_set(labelled_formula.formula, rule_names)

def get_sequent_immediate_children(sequent : Sequent, rule_names):
    # Merge the immediate children
    immediate_children = set()
    
    for antecedent in sequent.antecedents:
        if isinstance(antecedent, LabelledFormula):
            antecedent_immediate_children = get_labelled_formula_immediate_children(antecedent, rule_names)
            immediate_children |= set(antecedent_immediate_children)
    
    for consequent in sequent.consequents:
        if isinstance(consequent, LabelledFormula):
            consequent_immediate_children = get_labelled_formula_immediate_children(consequent, rule_names)
            immediate_children |= set(consequent_immediate_children)

    return immediate_children

def smart_replace(input, replacement_function, old_list, new_list):
    assert len(old_list) == len(new_list)

    intermediate_names = ['_' + str(i) + '_' for i in range(len(old_list))]

    for old_name, intermediate_name in zip(old_list, intermediate_names):
        input = replacement_function(input, old_name, intermediate_name)
    
    for intermediate_name, new_name in zip(intermediate_names, new_list):
        input = replacement_function(input, intermediate_name, new_name)
    
    return input

def replace_labels(sequent : Sequent, label_pairing):
    old_labels = [pair[0] for pair in label_pairing]
    new_labels = [pair[1] for pair in label_pairing]

    return smart_replace(sequent, lambda input, old, new: input.replace_label(old, new), old_labels, new_labels)

def replace_prop_variables(sequent : Sequent, prop_variable_pairing):
    old_prop_variables = [pair[0] for pair in prop_variable_pairing]
    new_prop_variables = [pair[1] for pair in prop_variable_pairing]

    return smart_replace(sequent, lambda input, old, new: input.replace_prop_variable(old, new), old_prop_variables, new_prop_variables)

def replace_semantic_variables(sequent : Sequent, semantic_variable_pairing):
    old_semantic_variables = [pair[0] for pair in semantic_variable_pairing]
    new_semantic_variables = [pair[1] for pair in semantic_variable_pairing]

    return smart_replace(sequent, lambda input, old, new: input.replace_semantic_variable(old, new), old_semantic_variables, new_semantic_variables)

class ExtraMultisetType(Enum):
    GAMMA = 0
    DELTA = 1

class ChildSequent(Sequent):
    def __init__(self, antecedents: Union[List[LabelledFormula], Set[LabelledFormula]], consequents: Union[List[LabelledFormula], Set[LabelledFormula]], extra_antecedents : Union[Set[ExtraMultisetType], List[ExtraMultisetType]], extra_consequents : Union[Set[ExtraMultisetType], List[ExtraMultisetType]]) -> None:
        super().__init__(antecedents, consequents)

        if isinstance(extra_antecedents, list):
            self.extra_antecedents = set(extra_antecedents)
        if isinstance(extra_consequents, list):
            self.extra_consequents = set(extra_consequents)

        self.extra_antecedents = extra_antecedents
        self.extra_consequents = extra_consequents
    
    def replace_prop_variable(self, old : str, new : str) -> 'ChildSequent':
        sequent = super().replace_prop_variable(old, new)
        return ChildSequent(sequent.antecedents, sequent.consequents, self.extra_antecedents, self.extra_consequents)

    def replace_semantic_variable(self, old : str, new : str) -> 'ChildSequent':
        sequent = super().replace_semantic_variable(old, new)
        return ChildSequent(sequent.antecedents, sequent.consequents, self.extra_antecedents, self.extra_consequents)

    def replace_label(self, old : str, new : str) -> 'ChildSequent':
        sequent = super().replace_label(old, new)
        return ChildSequent(sequent.antecedents, sequent.consequents, self.extra_antecedents, self.extra_consequents)

    def clone(self) -> 'ChildSequent':
        sequent = super().clone()
        return ChildSequent(sequent.antecedents, sequent.consequents, self.extra_antecedents, self.extra_consequents)

    def __str__(self) -> str:
        extra_antecedents = []

        if ExtraMultisetType.GAMMA in self.extra_antecedents:
            extra_antecedents.append('Γ')
        if ExtraMultisetType.DELTA in self.extra_antecedents:
            extra_antecedents.append('Δ')

        extra_consequents = []

        if ExtraMultisetType.GAMMA in self.extra_consequents:
            extra_consequents.append('Γ')
        if ExtraMultisetType.DELTA in self.extra_consequents:
            extra_consequents.append('Δ')

        return ', '.join([str(antecedent) for antecedent in list(self.antecedents) + extra_antecedents]) +  ' ⇒  ' + ', '.join([str(consequent) for consequent in list(self.consequents) + extra_consequents])
    
    __repr__ = __str__

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Sequent):
            return self.antecedents == other.antecedents and self.consequents == other.consequents
        return False
    
    def as_sequent(self) -> Sequent:
        return Sequent(self.antecedents, self.consequents)

# w:(A OR B), Gamma => Delta
# Figli: A, Gamma => Delta
#        B, Gamma => Delta

# v:(C OR (D AND E)), v:F => v:D
##### v:(C OR (D AND E)) => 
# v:F =>

# Etichette della regola: {w}
# Etichette del caso specifico: {v}
# Metavariabili semantiche della regola: {}
# Metavariabili semantiche del caso specifico: {}
# Variabili proposizionali della regola: {A, B}
# Figli diretti del caso specifico: {C, (D AND E)}

# A = C, B = C
# A = C, B = (D AND E)
# A = (D AND E), B = C
# A = (D AND E), B = (D AND E)

# v:(C OR C) =>
#### v:(C OR (D AND E)) =>
# v:((D AND E) OR C) =>


# v:C, Gamma => Delta
# v:(D AND E), Gamma => Delta

ALL_PROP_VARIABLES = list(string.ascii_uppercase)
ALL_SEMANTIC_VARIABLES = list(string.ascii_lowercase)

def get_fresh(n : int, fresh_variables : List[str], existing_variables : Iterable[str]):
    if n == 0:
        return []

    variables = []
    for variable in fresh_variables:
        if variable not in existing_variables:
            variables.append(variable)
            if len(variables) == n:
                break
    if len(variables) < n:
        raise Exception('Not enough variables')
    return variables

def get_fresh_prop_variables(n : int, existing_variables : Iterable[str]):
    return get_fresh(n, ALL_PROP_VARIABLES, existing_variables)

def get_fresh_semantic_variables(n : int, existing_variables : Iterable[str]):
    return get_fresh(n, ALL_SEMANTIC_VARIABLES, existing_variables)

class Rule:
    def __init__(self, name, root : Sequent, children : List[ChildSequent] = None):
        if children is None:
            children = []

        self.name = name
        self.root = root
        self.children = children

    @property
    def fresh_prop_variables(self):
        children_variables = set()
        for child in self.children:
            children_variables |= child.prop_variables()

        return children_variables - self.root.prop_variables()

    @property
    def fresh_semantic_variables(self):
        children_variables = set()
        for child in self.children:
            children_variables |= child.semantic_variables()

        return children_variables - self.root.semantic_variables()

    def apply(self, current_root : Sequent, rule_names : List[str]):
        matching_antecedent_sets = [s for s in utils.powerset(current_root.antecedents, True) if len(s) == len(self.root.antecedents)]
        matching_consequent_sets = [s for s in utils.powerset(current_root.consequents, True) if len(s) == len(self.root.consequents)]
        for antecedent_set in matching_antecedent_sets:
            for consequent_set in matching_consequent_sets:
                specific_sequent = Sequent(antecedent_set, consequent_set)
                matches = self.apply_specific(specific_sequent, current_root, rule_names)
                # print('Matches:',matches)

                if len(matches) > 0:
                    # Pick the first match
                    root, children = matches[0]

                    gamma = set([f for f in current_root.antecedents if f not in antecedent_set])
                    delta = set([f for f in current_root.consequents if f not in consequent_set])

                    final_children = []

                    for child in children:
                        if ExtraMultisetType.GAMMA in child.extra_antecedents:
                            child.antecedents |= gamma
                        if ExtraMultisetType.DELTA in child.extra_antecedents:
                            child.antecedents |= delta
                        if ExtraMultisetType.GAMMA in child.extra_consequents:
                            child.consequents |= gamma
                        if ExtraMultisetType.DELTA in child.extra_consequents:
                            child.consequents |= delta
                        
                        final_children.append(child)
                    
                    return root, [child.as_sequent() for child in final_children]
                    

    def apply_specific(self, specific_sequent : Sequent, full_sequent : Sequent, rule_names : List[str]) -> List[Tuple[Sequent, List[ChildSequent]]]:
        known_labels = specific_sequent.labels()
        known_immediate_children = get_sequent_immediate_children(specific_sequent, rule_names)
        known_semantic_variables = specific_sequent.semantic_variables()

        # print('Immediate children:', known_immediate_children)

        unknown_labels = self.root.labels()
        unknown_prop_variables = self.root.prop_variables() - self.fresh_prop_variables
        unknown_semantic_variables = self.root.semantic_variables()

        # Match unknown with known
        label_pairings = utils.get_pairings(unknown_labels, known_labels)
        prop_variable_pairings = utils.get_pairings(unknown_prop_variables, known_immediate_children)
        semantic_variable_pairings = utils.get_pairings(unknown_semantic_variables, known_semantic_variables)

        rule_children = self.children

        # Handle fresh prop variables
        stale_prop_variables = unknown_prop_variables | full_sequent.prop_variables()
        new_prop_variables = get_fresh_prop_variables(len(self.fresh_prop_variables), stale_prop_variables)
        fresh_prop_variable_pairing = [(unknown_fresh_prop_variable, new_prop_variable) for unknown_fresh_prop_variable, new_prop_variable in zip(self.fresh_prop_variables, new_prop_variables)]
        rule_children = [replace_prop_variables(child, fresh_prop_variable_pairing) for child in rule_children]

        # Handle fresh semantic variables
        stale_semantic_variables = unknown_semantic_variables | full_sequent.semantic_variables()
        new_semantic_variables = get_fresh_semantic_variables(len(self.fresh_semantic_variables), stale_semantic_variables)
        fresh_semantic_variable_pairing = [(unknown_fresh_semantic_variable, new_semantic_variable) for unknown_fresh_semantic_variable, new_semantic_variable in zip(self.fresh_semantic_variables, new_semantic_variables)]
        rule_children = [replace_semantic_variables(child, fresh_semantic_variable_pairing) for child in rule_children]

        # print('==')
        # print(str(specific_sequent))
        # print('==')

        matches = []

        for label_pairing in label_pairings:
            for prop_variable_pairing in prop_variable_pairings:
                for semantic_variable_pairing in semantic_variable_pairings:
                    adapted_root = self.root.clone()
                    adapted_children = [child.clone() for child in rule_children]

                    adapted_root = replace_labels(adapted_root, label_pairing)
                    adapted_children = [replace_labels(child, label_pairing) for child in adapted_children]

                    adapted_root = replace_prop_variables(adapted_root, prop_variable_pairing)
                    adapted_children = [replace_prop_variables(child, prop_variable_pairing) for child in adapted_children]

                    adapted_root = replace_semantic_variables(adapted_root, semantic_variable_pairing)
                    adapted_children = [replace_semantic_variables(child, semantic_variable_pairing) for child in adapted_children]

                    if adapted_root == specific_sequent:
                        # print('MATCH!')
                        matches.append((adapted_root, adapted_children))

                    # print(adapted_root)
                    # print(adapted_children)
        return matches