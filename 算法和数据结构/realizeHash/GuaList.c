#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <string.h>

#include "GuaList.h"

struct GuaNodeStruct {
    type value;
    char *key;
    GuaNode *next;
};

struct GuaListStruct {
    type length;
    GuaNode *next;
    GuaNode *tail;
};

// 在不同的函数间传递东西，只能申请内存了
// malloc 申请的内存一定要 free ，否则会导致内存泄漏
GuaList *
GuaListCreate(void) {
    GuaList *list = malloc(sizeof(GuaList));
    list->length = 0;
    list->next = NULL;
    list->tail = NULL;
    
    return list;
}

// 把一个 List 的数据打印出来
void
GuaListLog(GuaList *list) {
    GuaNode *l = list->next;
    printf("list is:");
    printf("[");
    while(l != NULL) {
        printf(" (%s: %d) ", l->key, l->value);
        l = l->next;
    }
    printf("]\n");
}

int
GuaListLength(GuaList *list) {
    return list->length;
}

bool
GuaListIsEmpty(GuaList *list) {
    if (list != NULL && list->length == 0) {
        return true;
    }
    return false;
}

bool
GuaListContainsKey(GuaList *list, char *key) {
    GuaNode * l = list->next;
    while (l != NULL) {
        if (l->key == key) {
            return true;
        }
        l = l -> next;
    }
    return false;
}

bool
GuaListContains(GuaList *list, type value) {
    GuaNode * l = list->next;
    while (l != NULL) {
        if (l->value == value) {
            return true;
        }
        l = l -> next;
    }
    return false;
}

void
GuaListAppend(GuaList *list, char *key, type value) {
    list->length++;
    GuaNode *l = list->next;
    GuaNode *p = l;
    GuaNode *node = malloc(sizeof(GuaNode));
    node->next = NULL;
    node->value = value;
    node->key = key;
    if (l == NULL) {
        list->next = node;
    } else{
        while(l != NULL){
            p = l;
            l = l->next;
        }
        p->next = node;
    }
}

void
GuaListPrepend(GuaList *list, type value) {
    GuaNode *n = malloc(sizeof(GuaNode));
    n->value = value;
    n->key = " ";
    n->next = NULL;
    list->length++;
    GuaNode *l = list->next;
    n->next = l;
    list->next = n;
}

type
GuaListFirstElement(GuaList *list) {
    return list->next->value;
}

type
GuaListValueByKey(GuaList *list, char *key) {
    GuaNode *l = list->next;
    while (l != NULL) {
        if (l->key == key) {
            return l->value;
        }
        l = l->next;
    }
    return -1;
}

void
GuaListRemoveFirstElement(GuaList *list) {
    list->length--;
    GuaNode *l = list->next;
    list->next = l->next;
    free(l);
}

int
GuaListIndexOfElement(GuaList *list, type value) {
    int index = -1;
    GuaNode *l = list->next;
    while (l != NULL) {
        index++;
        if (l->value == value) {
            break;
        }
        l = l->next;
    }
    if (l == NULL) {
        index = -1;
    }
    return index;
}

void
GuaListUpdate(GuaList *list, char *key, type value) {
    if (GuaListContainsKey(list, key)) {
        GuaNode *l = list->next;
        while (l != NULL) {
            if (l->key == key) {
                l->value = value;
            }
            l = l->next;
        }
    }
}

void
GuaListInsertElementAtIndex(GuaList *list, type value, int index) {
    GuaNode *l = list->next;
    int tag = 0;
    while(l != NULL){
        if(tag == index){
            GuaNode *node = malloc(sizeof(GuaNode));
            node->key = "";
            node->value = value;
            list->length++;
            node->next = l->next;
            l->next = node;
        }
        tag++;
        l = l->next;
    }
}

void
GuaListClear(GuaList *list) {
    while (list->length != 0) {
        GuaListRemoveFirstElement(list);
    }
}

void
GuaListRemove(GuaList *list) {
    GuaListClear(list);
    free(list);
    list = NULL;
}

bool
GuaListEqual(GuaList *list, int *value, int length) {
    if (list->length != length) {
//        printf("failure1: %d, %d, %d\n", length, list->length, sizeof(value));
        return false;
    } else {
        GuaNode *l = list->next;
        for (int i = 0; i < length; i++) {
            if (l->value != value[i]) {
//                printf("failure2");
                return false;
            }
            l = l->next;
        }
    }
    return true;
}

