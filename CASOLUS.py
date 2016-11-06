# CASOLUS lexical analizer and parser
import sys, math
sys.path.insert(0, "../..")

if sys.version_info[0] >= 3:
    raw_input = input

# Tokens names
tokens = (
    'VAR', 'FLOAT', 'INT',
)

# some arithmetic symbols
literals = ['=', '+', '-', '*', '/', '(', ')', '^']

# set Variables format
t_VAR = r'[a-zA-Z_][a-zA-Z0-9_]*'

# Set floating point structure
#   number '.' number                   -> example. 12.34
#   number '.' number 'e' '+/-' number  -> example. 12.34e+56 or 12.34E-56
#   number 'e' '+/-' number             -> example. 12E+34 or 12e-34
def t_FLOAT(t):
    r"((\d+(\.\d*)?)|\.\d+)([eE][+-]?[0-9]+)?"
    t.value = float(t.value)
    return t

# Set integer structure
def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = " \t"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
import ply.lex as lex
lex.lex()

# Parsing precedence rules
precedence = (
    ('left', '^'),
    ('left', '+', '-'),
    ('left', '*', '/'),
    ('right', 'UMINUS'),
)

names = {}


# Define the statement assign
def p_statement_assign(p):
    'statement : VAR "=" expression'
    names[p[1]] = p[3]


# Define statement expression
def p_statement_expr(p):
    'statement : expression'
    print(p[1])


# Define arithmetic expression
def p_expression_arith(p):
    '''expression : expression '^' expression
                  | expression '+' expression
                  | expression '-' expression
                  | expression '*' expression
                  | expression '/' expression'''
    if p[2] == '^':
        p[0] = math.pow(p[1], p[3])
    elif p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]


def p_expression_uminus(p):
    "expression : '-' expression %prec UMINUS"
    p[0] = -p[2]


# Group several expression by parenthesis
def p_expression_group(p):
    "expression : '(' expression ')'"
    p[0] = p[2]


# Define an expression as a integer
def p_expression_int(p):
    "expression : INT"
    p[0] = p[1]


# Define an expression as a float
def p_expression_float(p):
    "expression : FLOAT"
    p[0] = p[1]


# Define an experssion as a variable
def p_expression_var(p):
    "expression : VAR"
    try:
        p[0] = names[p[1]]
    except LookupError:
        print("Undefined variable '%s'" % p[1])
        p[0] = 0


def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")

import ply.yacc as yacc
yacc.yacc()

while 1:
    try:
        s = raw_input('CASOLUS > ')
    except EOFError:
        break
    if not s:
        continue
    yacc.parse(s)
