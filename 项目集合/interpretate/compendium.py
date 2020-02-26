import math
from util import Type, Token
from util import token_to_num

def log(*args, **kwargs):
    print(*args, **kwargs)


# 自定义汇编语言
# 寄存器
'''
00010000    ; x
00100000    ; y
00110000    ; z
'''

# 指令
'''
00000000    ; set 指令, 用于往寄存器中存一个数字
00000001    ; load 指令, 用于从内存中载入一个数据到寄存器中
00000010    ; 这是 add 指令,
00000011    ; save 指令, 用于把寄存器里面的数据放到内存中
'''

# 内存
'''
00000000    ; 这是 a 内存地址
00000001    ; 这是 b 内存地址
00000010    ; 这是 c 内存地址
'''

global_cpu = {
    'x': '00010000',
    'y': '00100000',
    'z': '00110000'
}

global_neicun = {
    '@0': '00000000',
    '@1': '00000001',
    '@2': '00000010',
}


def decimalToBinary(val):
    if val == 0:
        return '0'
    if val == 1:
        return '1'
    mod = val % 2
    if mod == 1:
        mod = '1'
    else:
        mod = '0'
    n = math.floor(val / 2)
    return decimalToBinary(n) + mod


def zfill_0_n(s, size=8):
    length = size - len(s)
    s = ''
    for _ in range(length):
        s += '0'
    return s


def zfill(val):
    s = decimalToBinary(val)
    return zfill_0_n(s) + s


def setCmdHuibian(token_arr):
    cpu = token_arr[1].value
    val = token_to_num(token_arr[2])
    cmd = '00000000'
    cp = global_cpu.get(cpu)
    v = zfill(val)
    return cmd + cp + v


def saveCmdHuibian(token_arr):
    cpu = token_arr[1].value
    neicun = token_arr[2].value
    cmd = '00000011'
    cp = global_cpu.get(cpu)
    nc = global_neicun.get(neicun)
    return cmd + cp + nc


def loadCmdHuibian(token_arr):
    neicun = token_arr[1].value
    cpu = token_arr[2].value
    cmd = '00000001'
    cp = global_cpu.get(cpu)
    nc = global_neicun.get(neicun)
    return cmd + nc + cp


def addCmdHuibian(token_arr):
    cpu1 = token_arr[1].value
    cpu2 = token_arr[2].value
    cpu3 = token_arr[3].value
    cmd = '00000010'
    cp1 = global_cpu.get(cpu1)
    cp2 = global_cpu.get(cpu2)
    cp3 = global_cpu.get(cpu3)
    return cmd + cp1 + cp2 + cp3


huibianCmdsMap = {
    'set': setCmdHuibian,
    'save': saveCmdHuibian,
    'load': loadCmdHuibian,
    'add': addCmdHuibian,
}


def get_arr(tokens):
    i = 0
    status = False
    offset = 0
    while i < len(tokens):
        token = tokens[i]
        i += 1
        if token.type == Type.keyWord and (i - 1) != 0:
            status = True
        if status:
            offset = i - 2
            break
    if i == len(tokens):
        return tokens, len(tokens)
    return tokens[:i - 1], offset


def parsed_json(tokens):
    results = []
    length = len(tokens)
    i = 0
    while i < length:
        token = tokens[i]
        i += 1
        if token.type == Type.keyWord:
            value, offset = get_arr(tokens[i - 1:])
            results.append(value)
            i += offset
    return results


def huibianParsed(s):
    # log('result:{}'.format([n for n in s]))
    from ast_parsing import json_tokens
    json_s = json_tokens(s)
    # log('json', json_s)
    parsed_s = parsed_json(json_s)
    # log('parsed', parsed_s)
    result = ''''''
    for arr_token in parsed_s:
        keyword = arr_token[0]
        func = huibianCmdsMap.get(keyword.value)
        res = func(arr_token) + '\n'
        result += res
    return result


if __name__ == '__main__':
    s = """
        set x 0
        set y 2
        save x @0
        save y @1
        load @0 x
        load @1 y
        add x y z
        save z @2 
       """
    json_s = huibianParsed(s)
    log(json_s)
    pass
