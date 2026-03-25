grammar Main;

program: statement* EOF;
statement: letBinding | functionDecl | structDecl | ifStatement | whileStatement
         | printStatement
         | loopStatement | forStatement | breakStmt | continueStmt | expression ';';
forStatement: 'for' ID 'in' expression block;
whileStatement: 'while' expression block;
printStatement: 'println!' '(' STRING (',' expression)* ')' ';';
letBinding: 'let' 'mut'? ID (':' type)? '=' expression ';';
structDecl: 'struct' ID '{' (structField (',' structField)*)? '}';
structField: ID ':' type;
functionDecl: 'fn' ID '(' parameters? ')' ('->' type)? block;
parameters: parameter (',' parameter)*;
parameter: ID ':' type;
block: '{' statement* '}';
ifStatement: 'if' expression block ('else' (ifStatement | block))?;
loopStatement: 'loop' block;
breakStmt: 'break' ';';
continueStmt: 'continue' ';';
type: 'i32' | 'f64' | 'bool' | 'String' | 'Vec<' type '>' | ID;
expression: ID '(' arguments? ')'               # CallExpr
          | expression '.' ID '(' arguments? ')' # MethodExpr
          | expression '[' expression ']'       # IndexExpr
          | expression op=('*'|'/') expression  # BinaryExpr
          | expression op=('+'|'-') expression  # BinaryExpr
          | expression op=('=='|'!='|'<'|'>'|'<='|'>=') expression # CompareExpr
          | '(' expression ')'                  # GroupExpr
          | ID                                  # IdExpr
          | INT                                 # IntLiteral
          | FLOAT                               # FloatLiteral
          | STRING                              # StringLiteral
          | BOOL                                # BoolLiteral;
arguments: expression (',' expression)*;
ID: [a-zA-Z_][a-zA-Z0-9_]*;
INT: [0-9]+;
FLOAT: [0-9]+ '.' [0-9]+;
STRING: '"' .*? '"';
BOOL: 'true' | 'false';
WS: [ \t\r\n]+ -> skip;
COMMENT: '//' ~[\r\n]* -> skip;
