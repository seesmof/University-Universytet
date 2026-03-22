grammar Main;

program: item* EOF;
item: function | structDef | implBlock;
function: 'fn' ID '(' paramList? ')' ('->' type_)? block;
paramList: param (',' param)*;
param: ID ':' type_;
type_: primitiveType | 'Vec' '<' type_ '>' | ID;
primitiveType: 'i32' | 'bool' | 'String';
structDef: 'struct' ID '{' fieldList? '}';
fieldList: field (',' field)*;
field: ID ':' type_;
implBlock: 'impl' ID '{' method* '}';
method: function;
block: '{' statement* '}';
statement: letStmt | expr ';'? | ifStmt | forLoop | whileLoop | ';';
letStmt: 'let' ID (':' type_)? '=' expr ';';
ifStmt: 'if' expr block ('else' (block | ifStmt))?;
forLoop: 'for' ID 'in' expr '..' expr block;
whileLoop: 'while' expr block;
expr
    : expr binOp expr               # binaryExpr
    | unOp expr                     # unaryExpr
    | ID '(' exprList? ')'          # callExpr
    | expr '.' ID '(' exprList? ')' # methodCallExpr
    | expr '.' ID                   # fieldAccess
    | 'vec!' '[' exprList? ']'      # vecLiteral
    | literal                       # litExpr
    | ID                            # varExpr
    | '(' expr ')'                  # parenExpr
    ;
exprList: expr (',' expr)*;
literal: INT | STRING | 'true' | 'false';
binOp: '+' | '-' | '*' | '/' | '%' | '==' | '!=' | '<' | '>' | '<=' | '>=' | '&&' | '||';
unOp: '-' | '!';
ID: [a-zA-Z_][a-zA-Z0-9_]*;
INT: [0-9]+;
STRING: '"' .*? '"';
WS: [ \t\r\n] -> skip;
COMMENT: '//' ~[\r\n]* -> skip;