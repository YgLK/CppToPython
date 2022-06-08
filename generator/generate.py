# fmt: off
tokens = [
    # + - ++  --  *   /   %   \   )   (
    'PLUS', 'MINUS', 'DPLUS', 'DMINUS', 'MUL', 'DIV', 'MOD',

    # \  )  (   [     ]    {   } 
    'ESC', 'RPARENTH', 'LPARENTH', 'LSQUARE', 'RSQUARE', 'LBRACE', 'RBRACE',
    #  :   ;   ,   "   '   . 
    'COLON', 'SEMICOLON', 'COMMA',
    # 'QUOTE',  'APOSTROPHE', 
    'DOT',

    # > < ! =  == >= <= != << >>
    'GTHAN', 'LTHAN',
    # 'NOT', 
    'EQUAL', 'DEQUAL', 'GREATER_EQUAL', 'LESS_EQUAL', 'NOT_EQUAL',

    # << >>
    'LBIT', 'RBIT',

    # int float char string bool void true false
    'INT', 'FLOAT', 'CHAR', 'STRING', 'BOOL', 'VOID', 'TRUE', 'FALSE',

    # while for if else ,
    'WHILE', 'FOR', 'IF', 'ELSE',

    # cin cout main using namespace std include #
    'CIN', 'COUT', 'MAIN', 'USING', 'NAMESPACE', 'STD', 'INCLUDE', 'HASH',

    # return break
    'RETURN', 'BREAK',

    # continue delete endl ' 
    'CONTINUE', 'DELETE', 'ENDL',
    # class, public, private, protected
    'CLASS', 'PUBLIC', 'PRIVATE', 'PROTECTED',

    # VALUES - regex
    # int number
    'INTVAR',
    # variable name value    
    'VARNAME',
    # float number
    'FLOATVAR',

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
# t_QUOTE = r"\""
# t_APOSTROPHE = r"'"
t_DOT = r"\."

t_GTHAN = r">"
t_LTHAN = r"<"
# t_NOT = r"!"
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
t_TRUE = r"true"
t_FALSE = r"false"

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

t_CLASS = r"class"
t_PUBLIC = r"public"
t_PRIVATE = r"private"
t_PROTECTED = r"protected"

# # variable name value
# t_VARNAME = r"[a-zA-Z$][a-zA-Z_$0-9]*"
# text value
t_STRINGVAR = r"\"([^\\\n]|(\\.))*?\""
# comment
t_COMMENTVAR = r"^\/\/.*"

reserved = {
    "if": "IF",
    "then": "THEN",
    "else": "ELSE",
    "while": "WHILE",
    "int": "INT",
    "float": "FLOAT",
    "char": "CHAR",
    "bool": "BOOL",
    "main": "MAIN",
    "char": "CHAR",
    "cout": "COUT",
    "string": "STRING",
    "cin": "CIN",
    "void": "VOID",
    "true": "TRUE",
    "false": "FALSE",
    "return": "RETURN",
    "break": "BREAK",
    "continue": "CONTINUE",
    "delete": "DELETE",
    "endl": "ENDL",
    "using": "USING",
    "namespace": "NAMESPACE",
    "std": "STD",
    "include": "INCLUDE",
    "#": "HASH",
    "class": "CLASS",
    "public": "PUBLIC",
    "private": "PRIVATE",
    "protected": "PROTECTED",
    "for": "FOR",
    # TODO comlete the reserved tokens
}


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
        print("Float value too large %d", t.value)
        t.value = 0
    return t


# Ignored characters
t_ignore = " \t"


def t_VARNAME(t):
    r"[a-zA-Z_][a-zA-Z_0-9]*"
    t.type = reserved.get(t.value, "VARNAME")  # Check for reserved words
    return t


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
    (
        "nonassoc",
        "GTHAN",
        "LTHAN",
        "GREATER_EQUAL",
        "LESS_EQUAL",
        "NOT_EQUAL",
        "DEQUAL",
    ),
    ("left", "PLUS", "MINUS"),
    ("left", "MUL", "DIV", "MOD"),
    ("nonassoc", "DPLUS", "DMINUS"),
    ("left", "EQUAL"),
    ("right", "CLASS", "PRIVATE", "PROTECTED", "PUBLIC"),
)

# dictionary of names
names = {}


def p_error(t):
    print("Syntax error at '%s'" % t.value)


# ------------------------------------------------------------------------
s = str
tab = "    "


class ClassToken:
    def __init__(self, name):
        self.class_name = name
        self.class_fields = {}
        self.class_methods = {}

    def __str__(self):
        return f"""Class {self.class_name}:\n
            (Class fields: {self.class_fields},\n 
            Class methods: {self.class_methods})"""

    def __repr__(self):
        return self.__str__()


# S' -> "program"
# "program" = {"include"} "using_namespace_std" "block"
def p_program(t):
    """program : include using_namespace_std block
    | using_namespace_std block"""
    print(t[:])
    if len(t) == 4:
        t[0] = 3
    if len(t) == 3:
        t[0] = t[2]


# "block" = {"variable_def" | "class" | "function"} "main_func"
# "block" = {} "main_func"
def p_block(t):
    """block : block_part block_part main_func
    | main_func"""
    if len(t) == 4:
        t[0] = t[1:4]
    if len(t) == 2:
        t[0] = t[1]


def p_block_part(t):
    """block_part : variable_def
    | class
    | function
    | block_part block_part"""
    if len(t) == 2:
        t[0] = [t[1]]
    if len(t) == 3:
        t[0] = [t[1], t[2]]


# using_namespace_std = 'USING' 'NAMESPACE' 'STD' 'SEMICOLON'
def p_using_namespace_std(t):
    """using_namespace_std : USING NAMESPACE STD SEMICOLON"""
    pass


# "main_func" = ('VOID' | 'INT') 'MAIN' 'LPARENTH' 'RPARENTH' 'LBRACE' "func_block" 'RBRACE' 'SEMICOLON'
def p_main_func(t):
    """main_func : VOID MAIN LPARENTH RPARENTH LBRACE func_block RBRACE SEMICOLON
    | INT MAIN LPARENTH RPARENTH LBRACE func_block RBRACE SEMICOLON
    | INT MAIN LPARENTH RPARENTH LBRACE RBRACE SEMICOLON"""
    if len(t) == 9:
        t[0] = ["if __name__ == '__main__':", t[6]]
    if len(t) == 8:
        print("Main function in Python cannot be empty.")


# "parameters" = "type" 'VARNAME' {'COMMA' "type" 'VARNAME'}
def p_parameters(t):
    """parameters : type VARNAME
    | type VARNAME COMMA parameters"""
    if len(t) == 5:
        t[0] = [t[2]] + t[4]
    else:
        t[0] = [t[2]]


# "if_statement" = 'IF' 'LPARENTH' "condition" 'RPARENTH' 'LBRACE' "func_block" 'RBRACE' ["else_block"]
def p_if_statement(t):
    """if_statement : IF LPARENTH condition RPARENTH LBRACE func_block RBRACE else_block
    | IF LPARENTH condition RPARENTH LBRACE func_block RBRACE"""
    if len(t) == 9:
        if t[3] == True:
            t[0] = t[5]
        else:
            t[0] = t[8]
    elif len(t) == 8:
        if t[3] == True:
            t[0] = t[5]
        # else:
        #     t[0] = []


# "else_block" = 'ELSE' 'LBRACE' "func_block" 'RBRACE'
def p_else_block(t):
    """else_block : ELSE LBRACE func_block RBRACE"""
    # pass
    t[0] = t[3]


# "condition" = ('VARNAME' | "var_value") "comparator" ('VARNAME' | "var_value")
def p_condition(t):
    """condition : var_value comparator var_value
    | VARNAME comparator VARNAME
    | VARNAME comparator var_value
    | var_value comparator VARNAME"""
    try:
        if t[2] == "==":
            t[0] = t[1] == t[3]
        elif t[2] == "!=":
            t[0] = t[1] != t[3]
        elif t[2] == ">":
            t[0] = t[1] > t[3]
        elif t[2] == "<":
            t[0] = t[1] < t[3]
        elif t[2] == ">=":
            t[0] = t[1] >= t[3]
        elif t[2] == "<=":
            t[0] = t[1] <= t[3]
    except TypeError:
        print("Error: Cannot compare int and str types")
        t[0] = False


# "while_statement" = 'WHILE' 'LPARENTH' "condition" 'RPARENTH' 'LBRACE' "func_block" 'RBRACE'
def p_while_statement(t):
    "while_statement : WHILE LPARENTH condition RPARENTH LBRACE func_block RBRACE"


# "for_statement" = 'FOR' 'LPARENTH' 'INT' VARNAME EQUAL 'INTVAR' 'SEMICOLON' VARNAME "comparator" 'INTVAR' SEMICOLON VARNAME ('DPLUS' | 'DMINUS' | "math_operator" EQUAL 'INTVAR') 'LBRACE' "func_block" 'RBRACE' 'SEMICOLON'
def p_for_statement(t):
    """for_statement : FOR LPARENTH INT VARNAME EQUAL INTVAR SEMICOLON VARNAME comparator INTVAR SEMICOLON VARNAME math_operator EQUAL INTVAR RPARENTH LBRACE func_block RBRACE
    | FOR LPARENTH SEMICOLON SEMICOLON RPARENTH LBRACE func_block RBRACE"""


# "class" ='CLASS' 'VARNAME' "LBRACE" {"class_variables" | "class_functions"} "RBRACE" 'SEMICOLON'
def p_class(t):
    """class : CLASS VARNAME LBRACE class_variable class_functions RBRACE SEMICOLON
    | CLASS VARNAME LBRACE class_functions RBRACE SEMICOLON
    | CLASS VARNAME LBRACE class_variable RBRACE SEMICOLON"""


# "return_statement" = 'RETURN' ("var_value" |  'VARNAME') SEMICOLON
def p_return_satement(t):
    """return_statement : RETURN var_value SEMICOLON
    | RETURN SEMICOLON"""
    t[0] = t[2]


# "assign_var" = 'VARNAME' EQUAL "var_value" SEMICOLON
def p_assign_var(t):
    """assign_var : VARNAME EQUAL var_value SEMICOLON
    | VARNAME EQUAL calculation SEMICOLON"""
    names[t[1]] = t[3]


# "variable_def" = "declare_var" | "declare_assign_var"
def p_variable_def(t):
    """variable_def : declare_var
    | declare_assign_var"""


# "declare_assign_var" = "type" 'VARNAME' EQUAL "var_value" SEMICOLON
def p_declare_assign_var(t):
    """declare_assign_var : type VARNAME EQUAL var_value SEMICOLON
    | type VARNAME EQUAL calculation SEMICOLON"""
    names[t[2]] = t[4]
    t[0] = t[2:5]


# "declare_var" = "type" 'VARNAME' SEMICOLON
def p_declare_var(t):
    """declare_var : type VARNAME SEMICOLON"""
    # create default value of variable as 0
    names[t[2]] = 0
    t[0] = t[2:4]


# "class_variables" = ["access_modifier"] 'SEMICOLON'  {"variable_def"}
def p_class_variable(t):
    """class_variable : access_modifier COLON variable_def
    | variable_def
    | assign_var
    | class_variable class_variable"""
    # pass


# "class_functions" = ["access_modifier"] {"function"} 'SEMICOLON'
def p_class_functions(t):
    """class_functions : access_modifier COLON function
    | function
    | class_functions class_functions"""
    # pass


# "function" = "return_type" 'VARNAME' 'LPARENTH' ["parameters"] 'RPARENTH' 'LBRACE' "func_block" 'RBRACE' 'SEMICOLON'
def p_function(t):
    """function : return_type VARNAME LPARENTH parameters RPARENTH LBRACE func_block RBRACE
    | return_type VARNAME LPARENTH RPARENTH LBRACE func_block RBRACE"""
    # pass


# "access_modifier" = 'PUBLIC' | 'PRIVATE' | 'PROTECTED'
def p_access_modifier(t):
    """access_modifier : PUBLIC
    | PRIVATE
    | PROTECTED"""
    # pass


# "func_block" = ({"variable_def" | "if_statement" | "while_statement" | "for_statement | "print_out" | "cin_in" | "variable_def" | 'VARNAME' EQUAL "calculation" 'SEMICOLON' } | "return_statement")
# "func_block" = statement  | statement return_statement | "return_statement")
def p_func_block(t):
    """func_block : statement
    | statement return_statement
    | return_statement"""
    return t


# "statement" = "variable_def" | "if_statement" | "while_statement" | "for_statement | "print_out" | "cin_in" | "variable_def" | 'VARNAME' EQUAL "calculation" 'SEMICOLON'
def p_statement(t):
    """statement : variable_def
    | if_statement
    | while_statement
    | for_statement
    | print_out
    | cin_in
    | VARNAME EQUAL calculation SEMICOLON
    | assign_var
    | statement statement"""
    if len(t) == 2:
        t[0] = t[1]
    if len(t) == 5:
        t[0] = [t[1:]]
    if len(t) == 3:
        t[0] = t[1:]


# "print_out" = 'COUT' "cout_expression_string" 'SEMICOLON'
def p_print_out(t):
    """print_out : COUT cout_expression_string SEMICOLON"""
    t[0] = ["print(", t[2], ")"]


# "cout_expression_string" = 'cout_expression' "cout_expression_string" | 'cout_expression'
def p_cout_expression_string(t):
    """cout_expression_string : cout_expression cout_expression_string
    | cout_expression"""
    if len(t) == 3:
        if t[1] == "endl":
            t[1] = "\n"
        if t[2] == "endl":
            t[2] = "\n"
        # cut "" signs from string
        t[0] = t[1].replace('"', "") + t[2].replace('"', "")
    else:
        if t[1] == "endl":
            t[1] = "\n"
        t[0] = t[1].replace('"', "")


# "cout_expression" = 'LBIT' "printable"
def p_cout_expression(t):
    """cout_expression : LBIT printable"""
    t[0] = t[2]


# "printable" = var_value | VARNAME | 'ENDL' | 'STRINGVAR'
def p_printable(t):
    """printable : var_value
    | VARNAME
    | ENDL
    | STRINGVAR"""
    # print(t[1])
    t[0] = t[1]
    # if t[1] in names.keys:
    #     t[0] = names[t[1]]
    # else:
    #     t[0] = t[1]


# "calculation" = "number" "math_operator" "number"
def p_calculation(t):
    "calculation : number math_operator number"
    if type(t[1]) != "int":
        if t[1] in names.keys():
            t[1] = names[t[1]]
        else:
            try:
                t[1] = int(t[1])
            except ValueError:
                return
    if type(t[3]) != "int":
        if t[3] in names.keys():
            t[3] = names[t[1]]
        else:
            try:
                t[3] = int(t[3])
            except ValueError:
                return
    try:
        if t[2] == "+":
            t[0] = t[1] + t[3]
        elif t[2] == "-":
            t[0] = t[1] - t[3]
        elif t[2] == "*":
            t[0] = t[1] * t[3]
        elif t[2] == "/":
            t[0] = t[1] / t[3]
        elif t[2] == "%":
            t[0] = t[1] % t[3]
        elif t[2] == "^":
            t[0] = t[1] ** t[3]
        elif t[2] == "//":
            t[0] = t[1] // t[3]
    except TypeError:
        print("Error: Invalid calculation")
        t[0] = 0


# "include" =  'HASH' 'INCLUDE' 'LTHAN' 'STRINGVAR' 'GTHAN'
def p_include(t):
    "include : HASH INCLUDE LTHAN VARNAME GTHAN"
    # importing lbraries in our version of c++ doenst have useful effect
    # when running from python


# "type" = 'INT' | 'FLOAT' | 'CHAR' | 'STRING' | 'BOOL'
def p_type(t):
    """type : INT
    | FLOAT
    | CHAR
    | STRING
    | BOOL"""
    # explicit types are not used in python
    pass


# "cin_in" = 'CIN' 'RBIT' 'VARNAME' 'SEMICOLON'
def p_cin_in(t):
    "cin_in : CIN RBIT VARNAME SEMICOLON"
    input_val = "input()"
    # check if input is previously declared variable
    if input_val in names.keys():
        names[t[3]] = names[input_val]
    # check if input is a number
    elif input_val.isdigit():
        names[t[3]] = input_val
    # check if input is a string
    elif input_val[0] in ["'", '"'] and input_val[-1] in ["'", '"']:
        names[t[3]] = input_val
    # return error
    else:
        print("Error: Invalid input - variable not declared")
        return


# "number" = 'INTVAR' | 'FLOATVAR'
def p_number(t):
    """number : INTVAR
    | FLOATVAR"""
    t[0] = t[1]


# "return_type" = "type" | 'VOID'
def p_return_type(t):
    """return_type : type
    | VOID"""
    # python doesnt need to use return types
    pass
    # t[0] = t[1]


# "math_operator" = 'PLUS' | 'MINUS' | 'MUL' | 'DIV'
def p_math_operator(t):
    """math_operator : PLUS
    | MINUS
    | MUL
    | DIV
    | MOD"""
    t[0] = t[1]


# "comparator" = 'GTHAN' | 'LTHAN' | 'DEQUAL' | 'GREATER_EQUAL' | 'LESS_EQUAL' | 'NOT_EQUAL'
def p_comparator(t):
    """comparator : GTHAN
    | LTHAN
    | LESS_EQUAL
    | DEQUAL
    | GREATER_EQUAL
    | NOT_EQUAL"""
    t[0] = t[1]


# "var_value" = 'INTVAR' | 'FLOATVAR' | 'STRINGVAR' | 'CHARVAR' | 'BOOLVAR'
def p_var_value(t):
    """var_value : INTVAR
    | FLOATVAR
    | STRINGVAR
    | bool_value"""
    t[0] = t[1]
    # -----------------------------------------------------------------------------------------
    # test if variables are saved properly
    # for k, v in names.items():
    #     print("key: " + str(k) + " value: " + str(v))


# -----------------------------------------------------------------------------------------


# "bool_value" = 'TRUE' | 'FALSE'
def p_bool_value(t):
    """bool_value : TRUE
    | FALSE"""
    t[0] = t[1]


# ------------------------------------------------------------------------
import ply.yacc as yacc
import ply.lex as lex

parser = yacc.yacc()

lex.lex()

with open("cpp_code.txt", "r") as file:
    test_input = file.read().rstrip()
# print(test_input)

lex.input(test_input)

while True:
    tok = lex.token()
    print(tok)
    if not tok:
        break

ac = parser.parse(test_input)
print("Results:", ac)
print("Names:")
for k, v in names.items():
    print("key: " + str(k) + " value: " + str(v))
