//
//  GuaTest.c
//  realizeHash
//
//  Created by chen on 2019/6/1.
//  Copyright © 2019 chenwoyao. All rights reserved.
//

#include "GuaTest.h"

void
ensure(bool condition, const char *message) {
    // 条件成立
    if(!condition) {
        printf("测试失败: %s\n", message);
    }
}
