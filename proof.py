from typing import List

from base import Sequent
from colors import bcolors

class Node:
    def __init__(self, element : Sequent, rule_name : str, children : List['Node'], main_sequent: Sequent) -> None:
        self.element = element
        self.rule_name = rule_name
        self.children = children
        self.main_sequent = main_sequent

    def stringified(self, indent = 0):
        s = ' ' * indent + ('└' if indent > 0 else '') + str(self.element) + ' (' + self.rule_name + ')\n'
        for child in self.children:
            s += child.stringified(indent + 2)

        return s

    def print(self, is_last, indent = "", is_root = False):
        kids = self.children
        item = ''
        if self.rule_name in ['N/A', 'Loop']:
            item = bcolors.FAIL + str(self.element) + bcolors.ENDC
        else:
            for i,antecedent in enumerate(self.element.antecedents):
                if antecedent in self.main_sequent.antecedents:
                    item += bcolors.OKCYAN + str(antecedent) + bcolors.ENDC + (', ' if i < len(self.element.antecedents)-1 else '')
                else:
                    item += str(antecedent) + (', ' if i < len(self.element.antecedents)-1 else '')
            item += ' ⇒ '
            for i,consequent in enumerate(self.element.consequents):
                if consequent in self.main_sequent.consequents:
                    item += bcolors.OKCYAN + str(consequent) + bcolors.ENDC + (', ' if i < len(self.element.consequents)-1 else '')
                else:
                    item += str(consequent) + (', ' if i < len(self.element.consequents)-1 else '')

        if is_root:
            item = item
        else:
            item = indent + ('└╴' if is_last else '├╴') + item
            indent = indent + ('  ' if is_last else '│ ')

        item = '{:<38} {:>12}'.format(item, bcolors.HEADER + (' (' + self.rule_name + ')' if self.rule_name != 'N/A' else '') + bcolors.ENDC)
        if is_last and len(kids) == 0:
            item += '\n'
        print(item)
        
        for i,child in enumerate(kids):
            if i == len(kids) - 1:
                child.print(True, indent, False)
            else:
                child.print(False, indent, False)
    
    def find_counterexample(self):
        if self.rule_name in ['N/A', 'Loop']:
            return self.element
        else:
            for child in self.children:
                result = child.find_counterexample()
                if result is not None:
                    return result
            return None

    def __str__(self) -> str:
        return self.stringified()
    
    __repr__ = __str__