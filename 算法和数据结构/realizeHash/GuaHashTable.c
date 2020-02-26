#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <ctype.h>
#include "GuaHashTable.h"
#include "GuaList.h"

#define HashSize 32

struct GuaHashTableStruct {
    GuaList *table[HashSize];
};

type
Hash(char * key) {
    int sum = 0;
    for (int i = 0; i < strlen(key); i++) {
        int k = toascii(key[i]);
        sum += k;
    }
    return sum % HashSize;
}

// 创建并返回一个 hashtable
GuaHashTable *
GuaHashTableCreate(void) {
    GuaHashTable *tb = malloc(sizeof(GuaHashTable));
    for (int i = 0; i < HashSize; i++) {
        GuaList *l = GuaListCreate();
        tb->table[i] = l;
    }
    return tb;
}

void
GuaHashTableLog(GuaHashTable *table){
    for (int i = 0; i < HashSize; i++) {
        GuaListLog(table->table[i]);
    }
}

// 往 hashtbale 中设置一个值, GuaHashTable 只支持 int 类型的值
void
GuaHashTableSet(GuaHashTable *table, char *key, int value) {
    int hash = Hash(key);
    GuaList *l = table->table[hash];
    if (GuaListContainsKey(l, key)) {
        GuaListUpdate(l, key, value);
    } else {
        GuaListAppend(l, key, value);
    }
}

// 检查 hashtable 中是否存在这个 key
bool
GuaHashTableHas(GuaHashTable *table, char *key) {
    int hash = Hash(key);
    GuaList *l = table->table[hash];
    return GuaListContainsKey(l, key);
}

// 返回 hashtable 中 key 对应的值, 不考虑 key 不存在的情况,
// 用户应该用 GuaHashTableHas 自行检查是否存在
int
GuaHashTableGet(GuaHashTable *table, char *key) {
    int hash = Hash(key);
    GuaList *l = table->table[hash];
    return GuaListValueByKey(l, key);
}

// 销毁一个 hashtable
void
GuaHashTableRemove(GuaHashTable *table) {
    for (int i = 0; i < HashSize; i++) {
        GuaListRemove(table->table[i]);
    }
    free(table);
    table=NULL;
}


