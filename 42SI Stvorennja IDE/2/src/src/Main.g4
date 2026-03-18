grammar Main;

expr: expr ('+' | '-') expr | INT;

start: expr EOF;

INT: [0-9]+;
WS: [ \t\r\n]+ -> skip;