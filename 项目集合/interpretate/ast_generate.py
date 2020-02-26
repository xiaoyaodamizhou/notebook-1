from util import Token, Type
from ast_transforming import *


def lispArr(arr):
    op = arr[0]
    # log('list op', op, arr)
    if isinstance(op, list):
        op = lispArr(op)
    if isinstance(op, Token):
        op = op.value
    tokens = arr[1:]
    # log('tokens', op, tokens)
    result = None
    d = {
        '+': add,
        '-': reduce,
        '*': multipy,
        '/': division,
        'if': adjust,
        'log': logging,
        '>': logical,
        '<': logical,
        '=': logical,
        '!': logical,
        'set': set,
    }
    if op in d:
        pass
        if op == '>' or op == '<' or op == '=' or op == '!':
            result = d[op](op, tokens)
        elif op == 'set':
            d[op](tokens)
        else:
            result = d[op](tokens)
    # log('lisp result', result)
    return result
