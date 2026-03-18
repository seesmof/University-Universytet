grammar Main;

start: LBRACE EXPR RBRACE;
EXPR: '0'..'9'+;
LBRACE: '(';
RBRACE: ')';
