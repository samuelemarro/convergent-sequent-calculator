from typing import List, Union
from base import Sequent
from proof import Node
from rule import Rule

def solve(sequent: Sequent, rules : List[Union[Rule, List[Rule]]], rule_names : List[str]) -> Node:
    for i, rule_set in enumerate(rules):
        if not isinstance(rule_set, list):
            rule_set = [rule_set]
        
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

                return Node(sequent, rule.name, [solve(child, new_rules, rule_names) for child in children], main_sequent)
    return Node(sequent, 'N/A', [])
