from typing import List
from base import Sequent
from proof import Node
from rule import Rule

def solve(sequent: Sequent, rules : List[Rule], rule_names : List[str]) -> Node:
    for rule in rules:
        result = rule.apply(sequent, rule_names)
        if result is not None:
            main_sequent, children = result
            return Node(sequent, rule.name, [solve(child, rules, rule_names) for child in children], main_sequent)
    return Node(sequent, 'N/A', [], Sequent([],[]))