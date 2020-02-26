/*
 C 语言中的 #include 的意思实际上是复制整个文件的内容过来
 
 所以为了防止重复包含头文件, 必须使用这种套路写法
 
 在现代的 C 语言中有宏可以保证头文件只被包含一次
 但是惯用的写法还是这样
 */
#ifndef __GuaList_H__
#define __GuaList_H__

#include <stdbool.h>


// interface
// 声明 结构名, 类型
struct GuaNodeStruct;
typedef struct GuaNodeStruct GuaNode;
struct GuaListStruct;
typedef struct GuaListStruct GuaList;
typedef int type;


GuaList *
GuaListCreate(void);


void
GuaListLog(GuaList *list);

/*
 1.1
 返回一个 GuaList 的长度
 */
int
GuaListLength(GuaList *list);

/*
 判断一个 GuaList 是否为空
 */
bool
GuaListIsEmpty(GuaList *list);

/*
 1.2
 检查一个 GuaList 中是否存在某个元素
 */
bool
GuaListContains(GuaList *list, type element);

bool
GuaListContainsKey(GuaList *list, char *key);
/*
 1.3
 在 GuaList 的末尾添加一个元素
 */
void
GuaListAppend(GuaList *list, char *key, type value);

/*
 1.4
 在 GuaList 的头部添加一个元素
 */
void
GuaListPrepend(GuaList *list, type element);

type
GuaListFirstElement(GuaList *list);

type
GuaListValueByKey(GuaList *list, char *key);

void
GuaListRemoveFirstElement(GuaList *list);

/*
 1.5
 在一个 GuaList 中查找某个元素, 返回下标(序号)
 如果不存在, 返回 -1
 */
int
GuaListIndexOfElement(GuaList *list, type element);

/*
 1.6
 往一个 GuaList 中插入一个元素, 下标(序号) 为 index
 不考虑非法情况(下标大于长度)
 */
void
GuaListInsertElementAtIndex(GuaList *list, type element, int index);

/*
 时间复杂度 O(n), 删除List的所有元素(清空List)
 */
void
GuaListClear(GuaList *list);

/*
 删除List中所有元素并销毁List
 */
void
GuaListRemove(GuaList *list);


bool
GuaListEqual(GuaList *list1, int *element, int length);

void
GuaListUpdate(GuaList *list, char *key, type value);
#endif
