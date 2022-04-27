grammar SequentCalculus;

multiset: ( statement ',' multiset | statement );

labelledFormula: ( LABEL ':' formula);

atom: LABEL RELATION LABEL;

statement: ( labelledFormula | atom );

formula:
    '(' formula ')'
    | <assoc=right> BOX formula
    | <assoc=right> DIAMOND formula
    | <assoc=right> NOT formula
    | <assoc=right> formula AND formula
    | <assoc=right> formula OR formula
    | <assoc=right> formula IMPLIES formula
    | VARIABLE
    | BOT
    | INTERMEDIATE_REPLACEMENT_ID
;

antecedent: multiset;
consequent: multiset;

sequent: ( ARROW | antecedent ARROW | ARROW consequent | antecedent ARROW consequent );


ARROW: '=';
AND: '&';
OR: '|';
IMPLIES: '?';
NOT: '!';
BOX: '#';
DIAMOND: '^';
LABEL: [a-z];
VARIABLE: [A-P|Q-Z];
LPAREN: '(';
RPAREN: ')';
BOT: '@';
RELATION: '.';
INTERMEDIATE_REPLACEMENT_ID: '_' [0-9]+ '_';

WS : ' '+ -> skip;
SKIPPABLE : ('\r' | '\n') -> skip;