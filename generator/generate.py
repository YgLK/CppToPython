# fmt: off
tokens = [
    # + - ++  --  *   /   %   \   )   (
    'PLUS','MINUS','DPLUS','DMINUS','MUL','DIV','MOD',

    # \  )  (   [     ]    {   } 
    'ESC','RPARENTH','LPARENTH', 'LSQUARE','RSQUARE','LBRACE','RBRACE',
    #  :   ;   ,   "   '   . 
    'COLON','SEMICOLON','COMMA','QUOTE','APOSTROPHE','DOT',

    # > < ! ==  == >= <= != << >>
    'GTHAN','LTHAN','NOT','EQUAL','DEQUAL','GREATER_EQUAL','LESS_EQUAL','NOT_EQUAL',
    
    # << >>
    'LBIT','RBIT',

    # int float char string bool void 
    'INT','FLOAT','CHAR','STRING','BOOL','VOID',
    
    # while for if else
    'WHILE','FOR','IF','ELSE',

    # cin cout main using namespace std include #
    'CIN','COUT','MAIN','USING','NAMESPACE','STD','INCLUDE','HASH',
    
    # return break
    'RETURN','BREAK',

    # continue delete endl ' ' \n \t
    'CONTINUE','DELETE','ENDL','SPACE','BREAKLINE','TAB',
    # class, public, private, protected
    'CLASS','PUBLIC','PRIVATE','PROTECTED',

    # VALUES - regex
    # variable name value    
    'VARNAME',
    # float number
    'FLOATVAR',
    # int number
    'INTVAR',
    # string/text value
    'STRINGVAR',
    # comment value
    'COMMENTVAR'

# | Token      |           Regexp            |
# | ---------- | :-------------------------: |
# | VARNAME    | `^[a-zA-Z$][a-zA-Z_$0-9]*$` |
# | FLOATVAR   |     `^-?\d*\.{0,1}\d+$`     |
# | INTVAR     |          `^-?\d+$`          |
# | STRINGVAR  |          `^".*"$`           |
# | COMMENTVAR |          `^\/\/.*`          |
]
# fmt: on

# Tokens

t_PLUS = r"\+"
t_MINUS = r"-"
t_DPLUS = r"\+\+"
t_DMINUS = r"--"
t_MUL = r"\*"
t_DIV = r"/"
t_MOD = r"%"

t_ESC = r"\\"
t_RPARENTH = r"\)"
t_LPARENTH = r"\("
t_LSQUARE = r"\["
t_RSQUARE = r"]"
t_LBRACE = r"{"
t_RBRACE = r"}"
t_COLON = r":"
t_SEMICOLON = r";"
t_COMMA = r","
t_QUOTE = r"\""
t_APOSTROPHE = r"'"
t_DOT = r"\."

t_GTHAN = r">"
t_LTHAN = r"<"
t_NOT = r"!"
t_EQUAL = r"="
t_DEQUAL = r"=="
t_GREATER_EQUAL = r">="
t_LESS_EQUAL = r"<="
t_NOT_EQUAL = r"!="
t_LBIT = r"<<"
t_RBIT = r">>"

t_INT = r"int"
t_FLOAT = r"float"
t_CHAR = r"char"
t_STRING = r"string"
t_BOOL = r"bool"
t_VOID = r"void"
t_WHILE = r"while"
t_FOR = r"for"
t_IF = r"if"
t_ELSE = r"else"

t_CIN = r"cin"
t_COUT = r"cout"
t_MAIN = r"main"
t_USING = r"using"
t_NAMESPACE = r"namespace"
t_STD = r"std"
t_INCLUDE = r"include"
t_HASH = r"\#"
t_RETURN = r"return"
t_BREAK = r"break"

t_CONTINUE = r"continue"
t_DELETE = r"delete"
t_ENDL = r"endl"
# t_SPACE = r" "
# t_BREAKLINE = r"\n"
# t_TAB = r"\t"

t_CLASS = r"class"
t_PUBLIC = r"public"
t_PRIVATE = r"private"
t_PROTECTED = r"protected"

# # variable name value
# t_VARNAME = r"[a-zA-Z$][a-zA-Z_$0-9]*"
# text value
t_STRINGVAR = r"^\".*\"$"
# comment
t_COMMENTVAR = r"^\/\/.*"


def t_INTVAR(t):
    r"-?\d+"
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t


def t_FLOATVAR(t):
    r"-?\d*\.{0,1}\d+"
    try:
        t.value = float(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t


# Ignored characters
t_ignore = " \t"


def t_newline(t):
    r"\n+"
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
import ply.lex as lex

lexer = lex.lex()

# Parsing rules

precedence = (
    ("left", "PLUS", "MINUS"),
    ("left", "TIMES", "DIVIDE"),
    ("right", "UMINUS"),
)

# dictionary of names
names = {}


def p_statement_assign(t):
    "statement : NAME EQUALS expression"
    names[t[1]] = t[3]


def p_statement_expr(t):
    "statement : expression"
    print(t[1])


def p_expression_binop(t):
    """expression : expression PLUS expression
    | expression MINUS expression
    | expression TIMES expression
    | expression DIVIDE expression"""
    if t[2] == "+":
        t[0] = t[1] + t[3]
    elif t[2] == "-":
        t[0] = t[1] - t[3]
    elif t[2] == "*":
        t[0] = t[1] * t[3]
    elif t[2] == "/":
        t[0] = t[1] / t[3]


def p_expression_uminus(t):
    "expression : MINUS expression %prec UMINUS"
    t[0] = -t[2]


def p_expression_group(t):
    "expression : LPAREN expression RPAREN"
    t[0] = t[2]


def p_expression_number(t):
    "expression : NUMBER"
    t[0] = t[1]


def p_expression_name(t):
    "expression : NAME"
    try:
        t[0] = names[t[1]]
    except LookupError:
        print("Undefined name '%s'" % t[1])
        t[0] = 0


def p_error(t):
    print("Syntax error at '%s'" % t.value)


import ply.yacc as yacc
import ply.lex as lex

# parser = yacc.yacc()

# while True:
#     try:
#         s = input("calc > ")  # Use raw_input on Python 2
#     except EOFError:
#         break
#     parser.parse(s)

lex.lex()

# test_input = """x = 3 * 4 + 5 * 6"""
test_input = """
int main()
{
    char str[30];
    string hi;
    cout<<"Enter Your Name ";
    cin>>str;
    cout<<"Hello "<<str<<"This is sample code, 152.32";
    cout<<endl;
    return 0;
}
"""
lex.input(test_input)


while True:
    tok = lex.token()
    print(tok)
    if not tok:
        break
