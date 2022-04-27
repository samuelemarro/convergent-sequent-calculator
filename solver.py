from typing import List, Union
from base import Sequent
from proof import Node
from rule import Rule
import loop

def solve(sequent: Sequent, rules : List[Union[Rule, List[Rule]]], rule_names : List[str], previous_sequents : List[Sequent] = None) -> Node:
    if previous_sequents is None:
        previous_sequents = []

    rules = [rule_set if isinstance(rule_set, list) else [rule_set] for rule_set in rules]
    max_repetitions = max(
        [
            max([(len(rule.root.prop_variables())) for rule in rule_set])
        for rule_set in rules]
    )
    # Check for a loop
    for previous_sequent in previous_sequents:
        if loop.contracted_view(sequent, max_repetitions) == loop.contracted_view(previous_sequent, max_repetitions):
            return Node(sequent, 'Loop', [], sequent)

    for i, rule_set in enumerate(rules):
        for rule in rule_set:
            result = rule.apply(sequent, rule_names)
            if result is not None:
                main_sequent, children = result

                # Make the current rule the last one
                new_rule_set = list(rule_set)
                new_rule_set.remove(rule)
                new_rule_set.append(rule)

                # Set the new rules
                new_rules = list(rules)
                new_rules[i] = new_rule_set

                return Node(sequent, rule.name, [solve(child, new_rules, rule_names, previous_sequents + [sequent]) for child in children], main_sequent)
    return Node(sequent, 'N/A', [], Sequent([], []))
