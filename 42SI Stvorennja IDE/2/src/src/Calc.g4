grammar Calc;

expr: term (('+' | '-') term)*;
term: factor (('*' | '/') factor)*;
factor: NUMBER | '(' expr ')' | ('-' | '+') factor;

NUMBER: [0-9]+ ('.' [0-9]+)?;
WS: [ \t\r\n]+ -> skip;