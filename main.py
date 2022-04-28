import sys

import parsing
from rules import RULES
import solver

from colors import bcolors
from printer import print_msg_box

def main():
    _input = sys.argv[1]
    sequent = parsing.parse_sequent(_input)

    print(bcolors.UNDERLINE + str(sequent) + bcolors.ENDC)

    proof = solver.solve(sequent, RULES, [])

    counterexample = proof.find_counterexample()

    if counterexample is None:
        print(bcolors.OKGREEN + 'Statement is provable.' + bcolors.ENDC + '\n')
    else:
        print(bcolors.FAIL + 'Statement is not provable.' + bcolors.ENDC + '\n')
        msg = 'Counter-example: ' + '\n'
        for antecedent in counterexample.antecedents:
            msg += 'Set ' + str(antecedent) + ' to True' + '\n'
        for i,consequent in enumerate(counterexample.consequents):
            msg += 'Set ' + str(consequent) + ' to False' + ('\n' if i < len(counterexample.consequents) - 1 else '')
        print_msg_box(msg, indent=10)
        

    print("_____PROOF_____")
    proof.print(False, "", True)
    #print(sequent)

if __name__ == '__main__':
    main()