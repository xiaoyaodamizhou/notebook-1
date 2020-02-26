from enum import Enum


class Type(Enum):
    auto = 0  # : , { } [ ]
    colon = 1  # :
    comma = 2  # ,
    braceLeft = 3
    braceRight = 4  # {
    bracketLeft = 5  # [
    bracketRight = 6
    number = 7
    string = 8
    keyWord = 9  # true, false, null, if, yes, no, log, set
    operator = 10  # + - * /
    logical = 11  # > < = !
    semicolon = 12  # ;
    variable = 13  # 变量


class Token(object):
    def __init__(self, token_type, token_value):
        super(Token, self).__init__()
        d = {
            ':': Type.colon,
            ',': Type.comma,
            '{': Type.braceLeft,
            '}': Type.braceRight,
            '[': Type.bracketLeft,
            ']': Type.bracketRight,
        }
        if token_type == Type.auto:
            self.type = d[token_value]
        else:
            self.type = token_type
        self.value = token_value

    def __repr__(self):
        return '({})'.format(self.value)


def token_to_num(token):
    s = token.value
    i = int(s)
    return i


# 单个token转字符串
def token_to_str(token):
    s = token.value
    return s
