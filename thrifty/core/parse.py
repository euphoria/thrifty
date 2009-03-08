"""
Parser for thrift files
"""
from ply import yacc
from thrifty.core import lex


def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")


def parse(data, debug=0):
    tparser.error = 0
    parsed = tparser.parse(data, debug=debug)
    if tparser.error:
        return None
    return parsed


tokens = lex.tokens

tparser = yacc.yacc()
