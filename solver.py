from typing import List, Union
from base import Sequent
from colors import bcolors
import loop
from proof import Node
from rule import Rule
from rules import DEFAULT_RULES
import parsing
from printer import print_msg_box

def solve(sequent: Sequent, rules : List[Union[Rule, List[Rule]]], previous_sequents : List[Sequent] = None) -> Node:
    if previous_sequents is None:
        previous_sequents = []

    rules = [rule_set if isinstance(rule_set, list) else [rule_set] for rule_set in rules]
    max_repetitions = max(
        [
            max([(max(len(rule.root.antecedents), len(rule.root.consequents))) for rule in rule_set])
        for rule_set in rules]
    )
    # Check for a loop
    for previous_sequent in previous_sequents:
        if loop.contracted_view(sequent, max_repetitions) == loop.contracted_view(previous_sequent, max_repetitions):
            return Node(sequent, 'Loop', [], sequent)

    for i, rule_set in enumerate(rules):
        for rule in rule_set:
            result = rule.apply(sequent)
            if result is not None:
                main_sequent, children = result

                # Make the current rule the last one
                new_rule_set = list(rule_set)
                new_rule_set.remove(rule)
                new_rule_set.append(rule)

                # Set the new rules
                new_rules = list(rules)
                new_rules[i] = new_rule_set

                return Node(sequent, rule.name, [solve(child, new_rules, previous_sequents + [sequent]) for child in children], main_sequent)
    return Node(sequent, 'N/A', [], Sequent([], []))


def visual_proof(sequent_string : str, rules = None):
    if rules is None:
        rules = DEFAULT_RULES

    sequent = parsing.parse_sequent(sequent_string)

    print(bcolors.UNDERLINE + str(sequent) + bcolors.ENDC)

    proof = solve(sequent, rules)

    counterexample = proof.find_counterexample()

    if counterexample is None:
        print(bcolors.OKGREEN + 'Statement is provable.' + bcolors.ENDC + '\n')
    else:
        print(bcolors.FAIL + 'Statement is not provable.' + bcolors.ENDC + '\n')
        msg = 'Counter-example: ' + '\n'
        for antecedent in set(counterexample.antecedents):
            msg += 'Set ' + str(antecedent) + ' to True' + '\n'
        for i,consequent in enumerate(set(counterexample.consequents)):
            msg += 'Set ' + str(consequent) + ' to False' + ('\n' if i < len(counterexample.consequents) - 1 else '')
        print_msg_box(msg, indent=10)

    print("_____PROOF_____")
    proof.print(False, "", True)