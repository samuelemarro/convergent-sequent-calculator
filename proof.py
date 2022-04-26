from typing import List

from base import Sequent

class Node:
    def __init__(self, element : Sequent, rule_name : str, children : List['Node']) -> None:
        self.element = element
        self.rule_name = rule_name
        self.children = children

    def stringified(self, indent = 0):
        s = ' ' * indent + ('└' if indent > 0 else '') + str(self.element) + ' (' + self.rule_name + ')\n'
        for child in self.children:
            s += child.stringified(indent + 2)

        return s
    
    def find_counterexample(self):
        if self.rule_name == 'N/A':
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