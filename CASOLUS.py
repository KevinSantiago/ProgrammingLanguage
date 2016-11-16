# CASOLUS lexical analizer and parser
import sys, math
import NewMathSide

sys.path.insert(0, "../..")

if sys.version_info[0] >= 3:
    raw_input = input


reserved = {
    'integration': 'INTEGRAL',
    'from': 'FROM',
    'to': 'TO',
    'derivation': 'DERIVATIVE',
    'limit' : 'LIMIT',
    'when': 'WHEN',
    'of' : 'OF',
    'oo' : 'INFINITY',
    'summation' : 'SUMMATION',
    'x' : 'XVALUE',
    # 'y' : 'YVALUE',
    # 'z' : 'ZVALUE',
    # 't' : 'TVALUE',
    'product' : 'PRODUCT',
}

# Tokens names
tokens = [
    'VAR',
    'FLOAT',
    'INT',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'POWER',
    'LPAREN',
    'RPAREN',
    'EQUALS',
    'GHOST',
    'ASSIGNMENT'
         ] + list(reserved.values())

# set Variables format
# Set tokens representation
t_PLUS = r'\+'
t_MINUS = '\-'
t_TIMES = r'\*'
t_DIVIDE = r'\/'
t_POWER = r'\^'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_EQUALS = r'\='
t_ASSIGNMENT = r'\<-'
t_GHOST = r'\->'
t_ignore = " \t"

def t_VAR(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'VAR')    # Check for reserved words
    return t

# Set floating point structure
#   number '.' number                   -> example. 12.34
#   number '.' number 'e' '+/-' number  -> example. 12.34e+56 or 12.34E-56
#   number 'e' '+/-' number             -> example. 12E+34 or 12e-34
def t_FLOAT(t):
    r'[+-]?([0-9]+)?([.][0-9]+)([eE][+-]?[0-9]+)?'
    t.value = float(t.value)
    return t

# Set integer structure
def t_INT(t):
    r'[+-]?[0-9]+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    print ("ERROR: Line %d: LEXER: Illegal character '%s' " % (t.lexer.lineno, t.value[0]))
    t.lexer.skip(1)

def t_COMMENT(t):
    r'\#.*'
    pass
    # No return value. Token discarded

# Build the lexer



import ply.lex as lex
lexer = lex.lex()


# Parsing precedence rules
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('left', 'POWER'),
    ('right', 'UMINUS'),
)

names = {}

# Define the statement assign
def p_statement_assign(p):
    'statement : VAR EQUALS expression'
    names[p[1]] = p[3]


def p_statement_assignTemp(p):
    'statement : VAR ASSIGNMENT'
    string = lexer.lexdata
    index =  string.index('<-')
    string = string[(index+2):]
    names[p[1]] = string


# Define statement expression
def p_statement_expr(p):
    'statement : expression'
    output = NewMathSide.reformateq(str(p[1]))


def p_expression_integral(p):
    'expression : INTEGRAL OF expression'


    if s.find('^') != -1:
        eq = NewMathSide.formateq(p[3])
    else:
        eq = str(p[3])
    eq = (str(NewMathSide.newintegration(eq, NewMathSide.symbols('x'))))
    eq = NewMathSide.reformateq(eq)
    p[0] = eq

def p_expression_definite_integral(p):
    'expression : INTEGRAL FROM expression TO expression OF expression'

    lowerBound = str(p[3])
    highBound = str(p[5])
    eq1 = str(p[7])
    if s.find('^') != -1:
        eq = NewMathSide.formateq(eq1)
    else:
        eq = str(eq1)
    eq =(str(NewMathSide.newintegration(eq, (NewMathSide.symbols('x'), lowerBound, highBound))))
    eq = NewMathSide.reformateq(eq)
    p[0] = eq


def p_expression_derivative(p):
    'expression : DERIVATIVE OF expression'

    if s.find('^') != -1:
        eq = NewMathSide.formateq(p[3])
    else:
        eq = str(p[3])
    eq = (str(NewMathSide.newderivative(eq, NewMathSide.symbols('x'))))
    eq = NewMathSide.reformateq(eq)
    p[0] = eq



def p_expression_limit(p):
    '''expression : LIMIT WHEN XVALUE GHOST expression OF expression
                    | LIMIT WHEN XVALUE GHOST INFINITY OF expression'''

    limitOf = str(p[3])
    tendsTo = str(p[5])
    eq1 = str(p[7])

    if s.find('^') != -1:
        eq = NewMathSide.formateq(eq1)
    else:
        eq = str(eq1)
    eq = (str(NewMathSide.limits(eq, NewMathSide.symbols('x'), tendsTo)))
    eq = NewMathSide.reformateq(eq)
    p[0] = eq



def p_expression_summation(p):
    'expression : SUMMATION FROM expression TO expression OF expression'

    lowerBound = p[3]
    highBound = p[5]
    eq1 = str(p[7])
    if s.find('^') != -1:
        eq = NewMathSide.formateq(eq1)
    else:
        eq = str(eq1)

    p[0] = NewMathSide.summation(eq, lowerBound, highBound, NewMathSide.symbols('x'))

def p_expression_product(p):
    'expression : PRODUCT FROM expression TO expression OF expression'

    lowerBound = p[3]
    highBound = p[5]
    eq1 = str(p[7])
    if s.find('^') != -1:
        eq = NewMathSide.formateq(eq1)
    else:
        eq = str(eq1)

    p[0] = NewMathSide.productnotation(eq, lowerBound, highBound, NewMathSide.symbols('x'))




def p_expression_basicMath(p):
    '''expression : expression PLUS expression
                   | expression MINUS expression
                   | expression POWER expression
                   | expression TIMES expression
                   | expression DIVIDE expression'''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '^':
        p[0] = math.pow(p[1], p[3])
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]


def p_expression_uminus(p):
    "expression : MINUS expression %prec UMINUS"
    p[0] = -p[2]


# Group several expression by parenthesis
def p_expression_group(p):
    "expression : LPAREN expression RPAREN"
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
   #     print("Undefined variable '%s'" % p[1])
        p[0] = 0


def p_error(p):{}
   # if p:
   # print("Syntax error at '%s'" % p.value)
   # else:
   # print("Syntax error at EOF")

import ply.yacc as yacc
parser = yacc.yacc()

while True:
    try:
        s = raw_input('CASOLUS > ')
    except EOFError:
        break
    if not s:
        continue
    parser.parse(s)
