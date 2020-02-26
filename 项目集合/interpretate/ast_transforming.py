from util import *


def log(*args, **kwargs):
    print(*args, **kwargs)


global_vars = {}


def set(arr):
    key = arr[0]
    value = arr[1]
    from ast_generate import lispArr
    if key.type == Type.variable:
        if isinstance(value, list):
            value = lispArr(value)
            global_vars[key.value] = value
        else:
            # log('set', value.type, value)
            if value.type == Type.number:
                val = token_to_num(value)
                global_vars[key.value] = val
            if value.type == Type.string:
                val = token_to_str(value)
                global_vars[key.value] = val
            if value.type == Type.variable:
                val = global_vars.get(value.value)
                global_vars[key.value] = val


def adjust(arr):
    '''
    没有if 这个单项
    [[(if), [(>), (2), (1)], (3), (4)]]
    [[(if), (yes), [(log), (成功)], [(log), (没成功)]]]
    '''
    from ast_generate import lispArr
    choose = arr[0]
    a1 = arr[1]
    a2 = arr[2]
    if isinstance(choose, list):
        choose = lispArr(choose)
    if choose.value == 'yes':
        if isinstance(a1, list):
            a1 = lispArr(a1)
            return a1
        return a1.value
    if choose.value == 'no':
        if isinstance(a2, list):
            a2 = lispArr(a2)
            return a2
        return a2.value
    return a2.value


def logging(arr):
    from ast_generate import lispArr
    value = arr[0]
    if isinstance(value, list):
        value = lispArr(value)
        return value
    if value.type == Type.variable:
        return global_vars.get(value.value)
    return value.value


def logical(op, arr):
    '''
    >, <, =, !
    :return token
    '''
    r1 = Token(Type.keyWord, 'yes')
    r2 = Token(Type.keyWord, 'no')
    a1 = arr[0].value
    a2 = arr[1].value
    if op == '>':
        if a1 > a2:
            return r1
        else:
            return r2
    if op == '<':
        if a1 < a2:
            return r1
        else:
            return r2
    if op == '=':
        if a1 == a2:
            return r1
        else:
            return r2
    if op == '!':
        if a1 != a2:
            return r1
        else:
            return r2
    return r2


def add(arr):
    num = 0
    i = 0
    from ast_generate import lispArr
    while i < len(arr):
        token = arr[i]
        i += 1
        if isinstance(token, list):
            result = lispArr(token)
            num += result
        else:
            if token.type == Type.number:
                value = token_to_num(token)
                num += value
            if token.type == Type.variable:
                value = global_vars.get(token.value)
                if value:
                    num += value
                else:
                    # log('value', value, global_vars)
                    raise "variable not initial"
        # log('sum', num)
    # log('add', num)
    return num


def reduce(arr):
    from ast_generate import lispArr
    num = arr[0]
    if isinstance(num, list):
        num = lispArr(num)
    if num.type == Type.variable:
        num = global_vars.get(num.value)
    else:
        num = token_to_num(num)
    i = 1
    while i < len(arr):
        token = arr[i]
        i += 1
        if isinstance(token, list):
            result = lispArr(token)
            num -= result
        else:
            if token.type == Type.number:
                val = token_to_num(token)
                num -= val
            if token.type == Type.variable:
                val = global_vars.get(token.value)
                num -= val
        # log("reduce", num)
    return num


def multipy(arr):
    from ast_generate import lispArr
    num = 1
    i = 0
    while i < len(arr):
        token = arr[i]
        i += 1
        if isinstance(token, list):
            result = lispArr(token)
            num *= result
        if token.type == Type.number:
            value = token_to_num(token)
            num *= value
        if token.type == Type.variable:
            val = global_vars.get(token.value)
            num *= val
        else:
            pass
    return num


def division(arr):
    from ast_generate import lispArr
    num = arr[0]
    if isinstance(num, list):
        num = lispArr(num)
    if num.type == Type.variable:
        num = global_vars.get(num.value)
    i = 1
    while i < len(arr):
        token = arr[i]
        i += 1
        if isinstance(token, list):
            result = lispArr(token)
            num /= result
        if token.type == Type.number:
            value = token_to_num(token)
            num /= value
        if token.type == Type.variable:
            val = global_vars.get(token.value)
            num /= val
        else:
            pass
    return num
