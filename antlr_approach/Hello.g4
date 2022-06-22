grammar Hello;

program:
	include using_namespace_std block
	| using_namespace_std block;

block: block_part main_func | main_func;

block_part:
	block_part block_part
	| variable_def
	| function
	| class_object;

main_func:
	return_type MAIN LPARENTH RPARENTH LBRACE func_block RBRACE
	| return_type MAIN LPARENTH RPARENTH LBRACE RBRACE;

using_namespace_std: USING NAMESPACE STD SEMICOLON;

class_object:
	CLASS VARNAME LBRACE class_variable class_functions RBRACE SEMICOLON
	| CLASS VARNAME LBRACE class_functions RBRACE SEMICOLON
	| CLASS VARNAME LBRACE class_variable RBRACE SEMICOLON;

class_variable:
	access_modifier COLON variable_def
	| variable_def
	| assign_var
	| class_variable class_variable;

class_functions:
	access_modifier COLON function
	| function
	| class_functions class_functions;

function:
	return_type VARNAME LPARENTH parameters RPARENTH LBRACE func_block RBRACE
	| return_type VARNAME LPARENTH RPARENTH LBRACE func_block RBRACE;

parameters:
	data_type VARNAME
	| data_type VARNAME COMMA parameters;

access_modifier: PUBLIC | PRIVATE | PROTECTED;

statement:
	func_call
	| variable_def
	| if_statement
	| while_statement
	| for_statement
	| print_out
	| cin_in
	| VARNAME EQUAL calculation SEMICOLON
	| assign_var
	| statement statement;

assign_var:
    VARNAME EQUAL VARNAME PLUS VARNAME SEMICOLON
    | VARNAME EQUAL VARNAME PLUS var_value SEMICOLON
    | VARNAME EQUAL var_value PLUS VARNAME SEMICOLON
	| VARNAME EQUAL var_value SEMICOLON
	| VARNAME EQUAL calculation SEMICOLON
	| VARNAME EQUAL VARNAME SEMICOLON;

for_statement:
	FOR LPARENTH INT VARNAME EQUAL INTVAR SEMICOLON VARNAME comparator INTVAR SEMICOLON VARNAME
		math_operator EQUAL INTVAR RPARENTH LBRACE func_block RBRACE
	|FOR LPARENTH INT VARNAME EQUAL INTVAR SEMICOLON VARNAME comparator VARNAME SEMICOLON VARNAME
		math_operator EQUAL INTVAR RPARENTH LBRACE func_block RBRACE
	|FOR LPARENTH VARNAME EQUAL INTVAR SEMICOLON VARNAME comparator VARNAME SEMICOLON VARNAME
		math_operator EQUAL INTVAR RPARENTH LBRACE func_block RBRACE
	| FOR LPARENTH SEMICOLON SEMICOLON RPARENTH LBRACE func_block RBRACE;

while_statement:
	WHILE LPARENTH condition RPARENTH LBRACE func_block RBRACE;

if_statement:
	IF LPARENTH condition RPARENTH LBRACE func_block RBRACE else_block
	| IF LPARENTH condition RPARENTH LBRACE func_block RBRACE;

else_block: ELSE LBRACE func_block RBRACE;

func_block:
	statement
	| statement return_statement
	| return_statement;

return_statement:
	RETURN var_value SEMICOLON
	| RETURN VARNAME SEMICOLON
	| RETURN SEMICOLON;

condition:
	var_value comparator var_value
	| VARNAME comparator VARNAME
	| VARNAME comparator var_value
	| var_value comparator VARNAME;

variable_def: declare_var | declare_assign_var;

declare_var: data_type VARNAME SEMICOLON;

declare_assign_var:
    data_type VARNAME EQUAL VARNAME math_operator VARNAME SEMICOLON
	|data_type VARNAME EQUAL var_value SEMICOLON
	| data_type VARNAME EQUAL calculation SEMICOLON;

print_out: COUT cout_expression_string SEMICOLON;

cout_expression_string:
	cout_expression cout_expression_string
	| cout_expression;

func_call:
    VARNAME LPARENTH func_call_parameters RPARENTH SEMICOLON
    | VARNAME LPARENTH RPARENTH SEMICOLON;

func_call_parameters:
    VARNAME COMMA func_call_parameters
    | VARNAME;

cout_expression: LBIT printable;

printable: var_value | VARNAME | ENDL | STRINGVAR;

calculation: number math_operator number;

include: HASH INCLUDE LTHAN VARNAME GTHAN;

cin_in: CIN RBIT VARNAME SEMICOLON;

number: INTVAR | FLOATVAR;

return_type: data_type | VOID;

data_type: INT | FLOAT | CHAR | STRING | BOOL;

math_operator: PLUS | MINUS | MUL | DIV | MOD;

comparator:
	GTHAN
	| LTHAN
	| LESS_EQUAL
	| DEQUAL
	| GREATER_EQUAL
	| NOT_EQUAL;

var_value: INTVAR | FLOATVAR | STRINGVAR | bool_value;

bool_value: TRUE | FALSE;

// tokens

WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines

PLUS: '+';
MINUS: '-';
DPLUS: '++';
DMINUS: '--';
MUL: '*';
DIV: '/';
MOD: '%';

ESC: '\\';
RPARENTH: ')';
LPARENTH: '(';
LSQUARE: '[';
RSQUARE: ']';
LBRACE: '{';
RBRACE: '}';
COLON: ':';
SEMICOLON: ';';
COMMA: ',';
DOT: '.';

GTHAN: '>';
LTHAN: '<';
EQUAL: '=';
DEQUAL: '==';
GREATER_EQUAL: '>=';
LESS_EQUAL: '<=';
NOT_EQUAL: '!=';
LBIT: '<<';
RBIT: '>>';

INT: 'int';
FLOAT: 'float';
CHAR: 'char';
STRING: 'string';
BOOL: 'bool';
VOID: 'void';
WHILE: 'while';
FOR: 'for';
IF: 'if';
ELSE: 'else';
TRUE: 'true';
FALSE: 'false';

CIN: 'cin';
COUT: 'cout';
MAIN: 'main';
USING: 'using';
NAMESPACE: 'namespace';
STD: 'std';
INCLUDE: 'include';
HASH: '#';
RETURN: 'return';
BREAK: 'break';

CONTINUE: 'continue';
DELETE: 'delete';
ENDL: 'endl';

CLASS: 'class';
PUBLIC: 'public';
PRIVATE: 'private';
PROTECTED: 'protected';


FLOATVAR: [0-9]* '.' [0-9]+;
INTVAR: '-'? [0-9]+;

VARNAME: [a-zA-Z_][a-zA-Z0-9_]*;

STRINGVAR: '"' .*? '"';

COMMENTVAR: DIV DIV VARNAME '\n';
