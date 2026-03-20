/*
 вбудовані типи даних, функції,
 вектори, записи, методи, цикли,
 умовні оператори, зв’язування
 змінних, арифметичні оператори
 */

grammar Main;

start: function | vector | method | block | params;
function: 'fn' NAME '(' NAME? ')' block;
vector: 'vec![' .*? ']';
method: 'impl' NAME block;
for: 'for' NAME 'in' NUMBER '..' NUMBER block;
loop: 'loop' block;
while: 'while' condition block;
condition: NAME COMPARISON_OPERATOR NUMBER;
if: 'if' NAME COMPARISON_OPERATOR NUMBER block;
let: 'let' NAME ('mut')? (':' type)? '=' NUMBER | NAME;
type: INT | UNT | FLOAT | BOOL | STR;
block: '{' .*? '}';
params: '(' .*? ')';

INT: 'i8' | 'i16' | 'i32' | 'i64' | 'i128';
UNT: 'u8' | 'u16' | 'u32' | 'u64' | 'u128';
FLOAT: 'f32' | 'f64';
BOOL: 'bool';
STR: 'str';
NUMBER: [0-9]+;
NAME: [a-zA-Z_]+;
COMPARISON_OPERATOR: '<' | '<=' | '>' | '>=' | '==' | '!=';
ARITHMETIC: '+' | '-' | '*' | '/';
WS: [ \r\t\n] -> skip;
STRING: '"' .*? '"';
SEMICOLON: ';';
LEFT_CURLY_BRACE: '{';
RIGHT_CURLY_BRACE: '}';