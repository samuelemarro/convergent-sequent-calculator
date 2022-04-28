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
Supported symbols:
  AND (alternatively /\\, \\/)
  OR (alternatively \\/, \\)
  NOT (alternatively ~, -)
  IMPLIES (alternatively ->)
  BOX (alternatively [])
  DIAMOND (alternatively <>)
  BOT (alternatively +)
  R (alternatively SEES)

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