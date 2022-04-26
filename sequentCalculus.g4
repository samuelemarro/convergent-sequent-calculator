multiset: ( statement ',' multiset | statement );
atom: LABEL RELATION LABEL;

statement: ( labelledFormula | atom );

