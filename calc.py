# -----------------------------------------------------------------------------
# calc.py
#
# A simple calculator for AoC 2020 day 18
# Adapted from https://github.com/dabeaz/ply
# -----------------------------------------------------------------------------
import ply.ply.lex as lex
import ply.ply.yacc as yacc

tokens = (
    'NUMBER',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'LPAREN', 'RPAREN',
)

# Tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


# Ignored characters
t_ignore = " \t"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    print(f"Illegal character {t.value[0]!r}")
    t.lexer.skip(1)


# Build the lexer
lex.lex()



def p_statement_expr(p):
    'statement : expression'
    p[0] = p[1]


def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]


def p_expression_uminus(p):
    'expression : MINUS expression %prec UMINUS'
    p[0] = -p[2]


def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]


def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]


def p_error(p):
    print(f"Syntax error at {p.value!r}")


def setup(precedence_type):
    if precedence_type == "EVEN":
        precedence = (
            ('left', 'TIMES', 'DIVIDE', 'PLUS', 'MINUS'),
            ('right', 'UMINUS'),
        )
    if precedence_type == "ADDITION_FIRST":
        precedence = (
            ('left', 'TIMES', 'DIVIDE'),
            ('left', 'PLUS', 'MINUS'),
            ('right', 'UMINUS'),
        )
    yacc.yacc()


def calculate(s):
    return yacc.parse(s)
