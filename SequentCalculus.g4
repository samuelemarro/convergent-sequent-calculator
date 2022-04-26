grammar SequentCalculus;

multiset: ( labelledFormula ',' multiset | labelledFormula );

labelledFormula: ( LABEL ':' formula);

formula: (
    | '(' formula ')'
    | '(' BOX formula ')'
    | '(' DIAMOND formula ')'
    | '(' NOT formula ')'
    | '(' formula AND formula ')'
    | '(' formula OR formula ')'
    | '(' formula IMPLIES formula ')'
    | VARIABLE
);

antecedent: multiset;
consequent: multiset;

sequent: ( ARROW | antecedent ARROW | ARROW consequent | antecedent ARROW consequent );


/*
ARROW: '=>';
AND: ( 'AND' | '/\\' );
OR: ( 'OR' | '\\/' );
IMPLIES: ( 'IMPLIES' | '->' );
NOT: ( 'NOT' | '~');
BOX: ( 'BOX' | '[]' );
DIAMOND: ( 'DIAMOND' | '<>' );
LABEL: [a-z];
VARIABLE: [A-Z];*/

ARROW: '=';
AND: '&';
OR: '|';
IMPLIES: '?';
NOT: '!';
BOX: '°';
DIAMOND: '^';
LABEL: [a-z];
VARIABLE: [A-Z];
LPAREN: '(';
RPAREN: ')';

WS : ' '+ -> skip;
SKIPPABLE : ('\r' | '\n') -> skip;