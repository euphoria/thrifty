"""
Parser for thrift files
"""
import ply.yacc as yacc
from thrifty.core import lex

tokens = lex.tokens

def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")

tparser = yacc.yacc()

def parse(data, debug=0):
    tparser.error = 0
    parsed = tparser.parse(data, debug=debug)
    if tparser.error:
        return None
    return parsed
