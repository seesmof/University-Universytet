grammar Main;

start: line+ EOF;
line: KEYWORD (NUM UNIT)+ NL;

KEYWORD: ('Lithium' | 'Potassium');
NUM: [0-9]+ ('.' [0-9]+)?;
UNIT: 'g/ml' | 'km' | 'W';
NL: '\n';
UNKNOWN: . -> skip;