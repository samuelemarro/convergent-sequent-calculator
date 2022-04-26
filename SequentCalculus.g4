grammar SequentCalculus;

multiset: ( statement ',' multiset | statement );

labelledFormula: ( LABEL ':' formula);

atom: LABEL RELATION LABEL;

statement: ( labelledFormula | atom );

formula: (
    | '(' formula ')'
    | '(' BOX formula ')'
    | '(' DIAMOND formula ')'
    | '(' NOT formula ')'
    | '(' formula AND formula ')'
    | '(' formula OR formula ')'
    | '(' formula IMPLIES formula ')'
    | VARIABLE
    | BOT
);

antecedent: multiset;
consequent: multiset;

sequent: ( ARROW | antecedent ARROW | ARROW consequent | antecedent ARROW consequent );


ARROW: '=';
AND: '&';
OR: '|';
IMPLIES: '?';
NOT: '!';
BOX: '°';
DIAMOND: '^';
LABEL: [a-z];
VARIABLE: [A-P|Q-Z];
LPAREN: '(';
RPAREN: ')';
BOT: '@';
RELATION: '.';

WS : ' '+ -> skip;
SKIPPABLE : ('\r' | '\n') -> skip;