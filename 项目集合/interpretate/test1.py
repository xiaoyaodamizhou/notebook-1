from ast_parsing import json_tokens, parsed_arrs, parsed_json
from ast_generate import lispArr


def log(*args, **kwargs):
    print(*args, **kwargs)


def test():
    ...


def test():
    s = """ 
    [+ 1 2]         ; 表达式的值是 3
    [* 2 3 4]       ; 表达式的值是 24
    [log "he\\\"llo"]   ; 输出 hello, 表达式的值是 null(关键字 表示空)
    [+ 1 [- 2 3]]   ; 表达式的值是 0, 相当于普通语法的 1 + (2 - 3)
    [+ 1 2 [- 3 4 5] [+ 4 5 6 7 8] [- 2 5]]  ; 表达式的值是 0
    [if [> 2 1] 3 4]; 表达式的值是 3
    [if yes
        [log "成功"]
        [log "没成功"]
    ];
        [set a 1]
        [set b 2]
        [+ a b];
        [set abc 123]
        [set edf 456]
        [set v1 [+ edf 456]]
        [/ v1 abc];
        [set v2 v1]
        [set v3 [+ v1 v2]]
        [log v3];
        """
    log(s)
    log('result:{}'.format([n for n in s]))
    jsonTokens = json_tokens(s)
    log('jsonTokens:', jsonTokens)
    results = parsed_json(jsonTokens)
    log('parsed_json:{}'.format(results))
    nextResults = parsed_arrs(results)
    log('nextResults: \n{}'.format('\n'.join([str(n) for n in nextResults])))
    for r in nextResults:
        if len(r) == 1:
            result = lispArr(r[0])
        else:
            for i in range(len(r)):
                result = lispArr(r[i])
        log(result)
    from ast_transforming import global_vars
    log('vars', global_vars)


if __name__ == '__main__':
    test()
