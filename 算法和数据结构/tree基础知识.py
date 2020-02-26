tree_definition= """
    树中节点数 = 总分叉数（节点数之和） + 1
    叶子节点的度数为0
    度就是指该节点的直接子节点有几个
    树的存储结构：{
        双亲表示法：
        孩子表示法：
        孩子兄弟表示法:
    } 
    完全二叉树： 从根结点到倒数第二层满足完美二叉树，最后一层可以不完全填充，其叶子结点都靠左对齐。
    
    二叉树第i层最多有2^(i-1)个节点
    二叉树深度为k最多有2^k-1个节点
    二叉树的终端结点数为n1，度数为2的结点数为n2,则n1=n2+1
    完全二叉树的结点数为n,则深度为lg2(n)+1
    
    二叉树和树和森林的转化：{
        树-》二叉树：
        1，加线，所有兄弟节点之间加一条线
        2，去线，树中每一个节点，只保留它与第一个孩子节点的连线，
            删除它与其他孩子节点的连线
        3，层次调整，以树的根节点为轴心，将整棵树旋转一定角度。
        第一个孩子是二叉树节点的左孩子，兄弟转换过来是节点➡右孩子
    }
    {
        森林->二叉树:
        1, 每个数变成二叉树
        2，每一颗二叉树不动，从第二颗二叉树的根节点作为前一个二叉树
        的根节点的右孩子，用联系那链接起来。
    }
    {
        二叉树->树:
        1,加线，（对存在左孩子a的节点n，如果该左孩子a有右孩子节点，将这些
            右孩子节点统统与节点n相连）
        2，去线，（删除二叉树中所有节点与其右孩子节点的连线）
    }
    {
        二叉树-》森林:
        1, 从根节点开始，若右孩子存在，则把与右孩子节点的连线删除，
        在查看分离后的二叉树，若右孩子存在，则连线删除，指导所有右孩子连线
        都删除为止，得到分离的二叉树。
        2，再将每课分离后的二叉树转换为树即可
    }
    {
        树与森林的遍历:
        
    }
    {
        赫夫曼树:
        
    }
"""

# 双亲表示法（顺序存储）
'''
#define MAX_TREE_SIZE 100
typedef int TElemType;
typedef struct PTNode{
    TElemType data;
    int parent;
}PTNode;

typedef struct{
    PTNode nodes[MAX_TREE_SIZE];
    int r, n;(根位置，结点数)
}PTree;
'''

# 孩子表示法（链式存储和顺序存储结合表示）
# 顺序存储（存放各个节点）
# 链式存储（存放节点的子节点）
'''
#define MAX_TREE_SIZE 100
typedef int TElemType;
typedef struct CTNode{
    int child;
    struct CTNode *next;
}*ChildPtr

typedef struct{
    TElemType data;
    ChildPtr firstchild;
}CTBox;

typedef struct{
    CTBox nodes[MAX_TREEE_SIZE];
    int r, n;
}CTree;
'''

# 孩子兄弟表示法(链式存储)
# data-firstchild-rightsib
'''
typedef struct CSNode{
    TElemType data;
    struct CSNode *firstchild, *rightchild;
}CSNode, *CSTree;
'''

# 二叉树的链表表示法
# lchild-data-rchild
'''
typedef struct BiTnode{
    TElemType data;
    struct BitNode *lchild, *rchild;
}BiTNode, *BiTree;
'''

# 二叉树前序遍历算法
'''
void PreOrderTraverse(BiTree T){
    if(T==NULL){
        return;
    }
    printf("%c", T->data);
    PreOrderTraverse(T->lchild);
    PreOrderTraverse(T->rchild);
}
'''

# 二叉树的初始化
'''
void CreateBiTree(BiTree *T){
    TElemType ch;
    scanf("%c", &ch);
    if(ch == '#'){
        *T = NULL;
    }else{
        *T = （BiTree)malloc(sizeof(BiTNode));
        if(!*T){
            exit(OVERFLOW);
        }
        (*T)->data = ch;
        CreateBiTree(&(*T)->lchild);
        CreateBiTree(&(*T)->rchild);    
    }
}
'''
