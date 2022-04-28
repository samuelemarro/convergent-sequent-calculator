from colors import bcolors
from solver import visual_proof

SPLASH_SCREEN = """

 ▄████████    ▄████████  ▄████████ 
███    ███   ███    ███ ███    ███ 
███    █▀    ███    █▀  ███    █▀  
███          ███        ███        
███        ▀███████████ ███        
███    █▄           ███ ███    █▄  
███    ███    ▄█    ███ ███    ███ 
████████▀   ▄████████▀  ████████▀  
                                   
==================================
   Convergent Sequent Calculator

  by Luca Donno and Samuele Marro
==================================

"""

HELP = """
Sequents are in the form
  label1:FORMULA1[, label2:FORMULA2...] => label3:FORMULA3[, label4:FORMULA4...]
(for labelled formulas). Relations can be written as label1Rlabel2.

Variables must be single-letter and uppercase (e.g. A, B...).
Labels must be single-letter and lowercase (e.g. a, b...).

Supported symbols:
  AND (alternatively /\\)
  OR (alternatively \\/)
  NOT (alternatively ~ or -)
  IMPLIES (alternatively ->)
  BOX (alternatively [])
  DIAMOND (alternatively <>)
  BOT (alternatively +)
  R (alternatively SEES) for relations

Examples:
  w:A AND B, w:A -> B => w:A
  w:A /\\ B, w R w => w:B, w:C
  w:[]A /\\ B, w R w => w:B, w:C
  w:DIAMOND A, u: BOX B => u:A
"""

def main():
    print(bcolors.OKBLUE + SPLASH_SCREEN + bcolors.ENDC)
    while True:
        print('Type a sequent to solve. Type "help" for more information or "exit" to quit.')
        print('> ', end='')
        command = input().strip()

        if command == 'exit':
            break
        elif command == 'help':
            print(HELP)
        else:
            visual_proof(command)
            print()

if __name__ == '__main__':
    main()