from util import Token, Type


def string_end(code, index):
    s = ''
    offset = index
    while offset < len(code):
        c = code[offset]
        if c == '"':
            return s, offset
        elif c == '\\':
            if code[offset + 1] == '"':
                s += '"'
                offset += 2
            if code[offset + 1] == 't':
                s += 't'
                offset += 2
            if code[offset + 1] == 'n':
                s += 'n'
                offset += 2
            else:
                pass
        else:
            s += c
            offset += 1
    pass


def json_tokens(code):
    length = len(code)
    tokens = []
    spaces = '\n\t\r'
    digits = '1234567890'
    keyWords = 'abcdefghigklmnopqrstuvwxyz@'
    logical = '><=!'
    operator = '+-*/'
    semicolon = ';'
    i = 0
    while i < length:
        c = code[i]
        i += 1
        if c in spaces:
            continue
        elif c in ':,{}[]':
            t = Token(Type.auto, c)
            tokens.append(t)
        elif c == '"':
            s, offset = string_end(code, i)
            i = offset + 1
            t = Token(Type.string, s)
            tokens.append(t)
        elif c in digits:
            end = 0
            for offset, char in enumerate(code[i:]):
                if char not in digits:
                    end = offset
                    break
            n = code[i - 1: i + end]
            i += end
            t = Token(Type.number, n)
            tokens.append(t)
        elif c in keyWords:
            t = ''
            offset = 0
            status = False
            if code[i - 1:i + 1] == 'if':
                # log('if')
                offset = 2 - 1
                t = Token(Type.keyWord, 'if')
                status = True
            elif code[i - 1:i + 2] == 'log':
                # log('log')
                offset = 3 - 1
                t = Token(Type.keyWord, 'log')
                status = True
            elif code[i - 1:i + 2] == 'yes':
                # log('yes')
                offset = 3 - 1
                t = Token(Type.keyWord, 'yes')
                status = True
            elif code[i - 1:i + 3] == 'true':
                # log('true')
                offset = 4 - 1
                t = Token(Type.keyWord, 'true')
                status = True
            elif code[i - 1:i + 4] == 'false':
                # log('false')
                offset = 5 - 1
                t = Token(Type.keyWord, 'false')
                status = True
            elif code[i - 1:i + 1] == 'no':
                # log('no')
                offset = 2 - 1
                t = Token(Type.keyWord, 'no')
                status = True
            elif code[i - 1:i + 3] == 'null':
                # log('null')
                offset = 4 - 1
                t = Token(Type.keyWord, 'null')
                status = True
            elif code[i - 1:i + 2] == 'set':
                # log('set')
                offset = 3 - 1
                t = Token(Type.keyWord, 'set')
                status = True
            elif code[i - 1:i + 2] == 'add':
                offset = 3 - 1
                t = Token(Type.keyWord, 'add')
                status = True
            elif code[i - 1:i + 3] == 'load':
                offset = 4 - 1
                t = Token(Type.keyWord, 'load')
                status = True
            elif code[i - 1:i + 3] == 'save':
                offset = 4 - 1
                t = Token(Type.keyWord, 'save')
                status = True
            else:
                n = i - 1
                while code[n] != ' ':
                    if code[n] == ']':
                        break
                    if code[n] in spaces:
                        break
                    n += 1
                offset = n - i
                t = Token(Type.variable, code[i - 1:n])
                status = True
            if status:
                i = offset + i
                tokens.append(t)
            else:
                pass
        elif c in operator:
            t = Token(Type.operator, c)
            tokens.append(t)
        elif c in logical:
            t = Token(Type.logical, c)
            tokens.append(t)
        elif c in semicolon:
            t = Token(Type.semicolon, c)
            tokens.append(t)
        else:
            pass
    return tokens


# 中间代码优化成代码块
def parsed_json(tokens):
    results = []
    length = len(tokens)
    i = 0
    j = 0
    while i < length:
        token = tokens[i]
        i += 1
        if token.type == Type.semicolon:
            right = j
            while j < i:
                if tokens[j].type == Type.bracketLeft:
                    right = j
                    break
                j += 1
            arr_token = tokens[right:i - 1]
            results.append(arr_token)
            j = i
    else:
        pass
    return results


# 代码块再加工
def get_array(tokens):
    '''
    [([), (+), (1), (2), ([), (-), (3), (4), (5), (]), ([), (+), (4), (5), (6), (7), (8), (]), (])]
    [([), (1), (2), (])]
    '''
    # log('get_array', tokens)
    i = 0
    offset = len(tokens) - 1
    count = 0
    status = False
    while i < len(tokens):
        token = tokens[i]
        i += 1
        if token.type == Type.bracketLeft:
            count += 1
            status = True
        elif token.type == Type.bracketRight:
            count -= 1
            status = True
        if count == 0 and status:
            offset = i - 1
            break
    return tokens[1:offset], offset


#  单个arr的tokens数组解析嵌套
def parsed_arr(arr):
    '''
    [([), (+), (1), (2), ([), (-), (3), (4), (5), ([), (+), (4), (5), (6), (7), (8), (]), (]), ([), (-), (2), (5), (]), (])]
    '''
    # log('arr', arr)
    i = 0
    ans = []
    if isinstance(arr, list):
        while i < len(arr):
            token = arr[i]
            i += 1
            if token.type == Type.bracketLeft:
                a, offset = get_array(arr[i - 1:])
                # log('old a', a)
                i = i + offset
                a = parsed_arr(a)
                # log('new a', a)
                ans.append(a)
            else:
                ans.append(token)
    else:
        return arr
    return ans


# 对含有多个tokens的arr数组做处理
def parsed_arrs(arrs):
    '''
    [([), (+), (1), (2), ([), (-), (3), (4), (5), (]), ([), (+), (4), (5), (6), (7), (8), (]), (])]
    [([), (if), (yes), ([), (log), (成功), (]), ([), (log), (没成功), (]), (])]
    [+ 1 2 [- 3 4 5] [+ 4 5 6 7 8] [- 2 5]];
    '''
    results = []
    for arr in arrs:
        if isinstance(arr, list):
            ans = parsed_arr(arr)
            arr = ans
            results.append(arr)
        else:
            return arrs
    return results
