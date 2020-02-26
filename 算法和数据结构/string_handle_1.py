def log(*args, **kwargs):
    print(*args, **kwargs)


# kmp
# 讲解见 http://www.ruanyifeng.com/blog/2013/05/Knuth–Morris–Pratt_algorithm.html
# 部分匹配表：
# 最后一个匹配字符的部分匹配值确定接下来搜索词的移动位数
# 移动位数 = 已匹配的字符数 - 对应的部分匹配值
# 有时候，字符串头部和尾部会有重复。比如，"ABCDAB"之中有两个"AB"，那么它的"部分匹配值"就是2（"AB"的长度）。
# 搜索词移动的时候，第一个"AB"向后移动4位（字符串长度-部分匹配值），就可以来到第二个"AB"的位置。

# 部分匹配表
def partial_table(p):
    '''
    partial_table("ABCDABD") -> [0, 0, 0, 0, 1, 2, 0]
    '''

    # 前缀和后缀, 最大公共字符串长度
    prefix = set()
    postfix = set()
    ret = [0]

    for i in range(1, len(p)):
        prefix.add(p[:i])
        postfix = {p[j:i + 1] for j in range(1, i + 1)}
        ret.append(len((prefix & postfix or {''}).pop()))
    return ret


def kmp_match(s, p):
    '''
    :param s:  字符串
    :param p: 搜索词
    :return: 坐标
    '''
    m = len(s)
    n = len(p)
    # 起始指针cur
    cur = 0
    table = partial_table(p)
    # 只去匹配 m - n 个
    while cur <= m - n:
        for i in range(n):
            if s[i + cur] != p[i]:
                cur += max(i - table[i - 1], 1)
                break
        # for 循环中，如果没有从任何一个 break 中退出，则会执行和 for 对应的 else
        # 只要从 break 中退出了，则 else 部分不执行。
        else:
            return cur
    return -1

def test_kmp():
    log(partial_table("ABCDABD"))
    log(kmp_match("BBC ABCDAB ABCDABCDABDE", "ABCDABD"))


##############################################################################
# 替换空格
def replaceSpace(fillchar, s):
    '''
    fillchar = %20''
    we are happy => We%20Are%20Happy
    '''
    temp = s.split(' ')
    result = fillchar.join(temp)
    return result

def test_replaceSpace():
    log(replaceSpace('%20', 'we are happy'))


##############################################################################
# 最长公共前缀
def hasStr(s, str):
    if s not in str:
        return False
    return True


def publicStr(str_list):
    result = ""
    firstStr = str_list[0]
    minum = min([len(s) for s in str_list])
    for i in range(1, minum + 1):
        subStr = firstStr[:i]
        for s in str_list:
            if not hasStr(subStr, s):
                break
        else:
            result = subStr
    return result

def testPubicStr():
    s = ["flower","flow","flight"]
    log(publicStr(s))

##############################################################################
# 最长回文串
def isEven(num):
    if num % 2 == 0:
        return True
    return False

def longestPalindRome(s):
    '''
    abccccdd => dccaccd
    构成回文的条件
    字符出现次数为双数的组合
    字符出现次数为双数的组合+一个只出现一次的字符
    '''
    keys = set(s)
    keys = [key for key in keys]
    obj = {}
    for key in keys:
        obj[key] = 0
    for n in s:
        for key in obj.keys():
            if key == n:
                obj[key] += 1
    sum = 0
    special = 0
    log('obj', obj)
    for key, val in obj.items():
        if isEven(val):
            sum += val
        else:
            special = max(special, val)
    return sum + special

def testLongestPalindRome():
    s = 'abccccdd'
    s1 = 'aaaadddeffffgggg'
    log(longestPalindRome(s), longestPalindRome(s1))


##############################################################################
# 验证回文串
def isPalindrome(s):
    '''
    abba True
    abab False
    '''
    specials = [',', ':', '[', ']', ' ']
    for special in specials:
        s = s.replace(special, '')
    s = s.lower()
    if s == s[::-1]:
        return True
    return False

def testIsPalindRome():
    s = "A man, a plan, a canal: Panama"
    log(isPalindrome(s))

##############################################################################
# 最长回文子串
def longestChildPalind(s):
    '''
    'bagagagaag'
    '''
    for i in range(len(s), 0, -1):
        length = i
        for j in range(len(s) - i + 1):
            n = s[j:j+length]
            if isPalindrome(n):
                return n
    return ''


def testLongestChildPalind():
    s1 = 'babad'
    s2 = 'cbbd'
    log(longestChildPalind(s1), longestChildPalind(s2))

##############################################################################
# 括号匹配深度
def scanner(str):
    '''
    (()())
    ((()))
    '''
    count = 0
    maxum = 0
    for s in str:
        if s == '(':
            count += 1
            maxum = max(maxum, count)
        else:
            count -= 1
    return maxum

def testScanner():
    s1 = '((()))'
    s2 = '(()())'
    log(scanner(s1), scanner(s2))

"""
数组去重：
const osort = (arr) => {
    let obj = {}
    for (let i = 0; i < arr.length; i++) {
        let a = arr[i]
        if (obj[a] === undefined) {
            obj[a] = 1
        }
        else if (obj[a]) {
            arr.splice(i, 1)
            i -= 1
        }
    }
    return arr
}
"""

if __name__ == '__main__':
    test_kmp()
    test_replaceSpace()
    testPubicStr()
    testLongestPalindRome()
    testIsPalindRome()
    testLongestChildPalind()
    testScanner()


