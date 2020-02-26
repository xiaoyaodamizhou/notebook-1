//
//  main.c
//  realizeHash
//
//  Created by chen on 2019/6/1.
//  Copyright © 2019 chenwoyao. All rights reserved.
//

#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#include "GuaList.h"
#include "GuaHashTable.h"
#include "GuaTest.h"

typedef int type;
GuaHashTable* table;


void
testGuaHashTableCreate() {
    printf("%s \n", "testGuaHashTableCreate begin");
    table = GuaHashTableCreate();
    GuaHashTableLog(table);
    printf("%s \n", "testGuaHashTableCreate end");
}

void
testGuaHashTableSet() {
    printf("set test:\n ");
    GuaHashTableSet(table, "woyao", 1);
    GuaHashTableSet(table, "woruo", 2);
    GuaHashTableSet(table, "wo", 3);
    GuaHashTableSet(table, "yao", 4);
    GuaHashTableSet(table, "a", 5);
    GuaHashTableSet(table, "A", 5);
    GuaHashTableLog(table);
}

void
testGuaHashTableHas() {
    printf("has test:\n ");
    bool adjsut = GuaHashTableHas(table, "woyao");
    printf("有没有:%d\n", adjsut);
}

void
testGuaHashTableGet() {
    printf("get test:\n");
    int value = GuaHashTableGet(table, "a");
    printf("key a is:%d\n", value);
}

void
testGuaHashTableRemove(){
    printf("remove test:\n");
    GuaHashTableRemove(table);
}

void testGuaHashTable() {
    testGuaHashTableCreate();

    testGuaHashTableSet();

    testGuaHashTableHas();

    testGuaHashTableGet();

    testGuaHashTableRemove();

}

int main(int argc, const char * argv[]) {
    // insert code here...
//    int a[] = {1, 2, 3};
//    int *p = a;
//    int length = sizeof(p) / sizeof(a[0]);
    
//    GuaList *l;
//    l = GuaListCreate();
//    GuaListLog(l);
//    GuaListAppend(l, "a", 1);
//    GuaListAppend(l, "b", 2);
//    GuaListAppend(l, "c", 3);
//    GuaListAppend(l, "d", 4);
//    GuaListLog(l);
//    GuaListAppend(l, "e", 5);
//    GuaListLog(l);
//    int arr[5] = {1, 2, 3, 4, 5};
//    int length = sizeof(arr) / sizeof(arr[0]);
//    bool adjust = GuaListEqual(l, arr, length);
//    printf("adjust: %d %d\n", adjust, length);
//    printf("length: %d\n", GuaListLength(l));
//    GuaListPrepend(l, 0);
//    GuaListLog(l);
//    GuaListUpdate(l, " ", -1);
//    GuaListLog(l);
//    printf("key c is: %d\n", GuaListValueByKey(l, "c"));
//    printf("value 6 is: %d\n", GuaListContains(l, 6));
//    printf("first: %d\n", GuaListFirstElement(l));
//    GuaListInsertElementAtIndex(l, 6, 5);
//    GuaListLog(l);
//
//    GuaListClear(l);
//    GuaListRemove(l);
//    GuaListLog(l);
//    printf("%d, %d\n", GuaListIsEmpty(l), GuaListLength(l));
    
    testGuaHashTable();
//    char a = 'a';
//    printf("%d", a);
//    const char * s = "adc";
//    printf("%d", s[1]);
//    int d = toascii(*s);
//    printf("%d\n", d);
//    char * s1 = "b";
//    int i = toascii(atoi(s));
//    printf("%d:%d", i, atoi(s1));
//    printf("len:%d", strlen(s));
    
    return 0;
}
