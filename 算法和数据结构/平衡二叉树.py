def log(*args, **kwargs):
    print(*args, **kwargs)


# （avl）平衡二叉树是在二叉搜索树（BST）上，对他的结构进行更好的处理
#  节点的结构体内增加了一个新的因子，平衡因子BF，大于一右旋，小于-1左旋
# 右旋
'''
     9         7
    / \         \
   7  10         9
    \           / \
     8         8  10
BitTree *p;
BitTree l;
l = (*p) -> lchild /* l指向p的左子树根节点 */
(*p)->lchild = l->rchild /* p的左子树为l的右子树*/
l->rchild = (*p) /*l的右子树为p*/
*p = l /*跟新根节点*/
'''

# 左旋
'''
     6         7
    / \       / 
   5   7     6  
            /
           5
BiTree *p;
BiTree r;
r = (*p)->rchild
(*p)->rchild = r->lchild
r->lchild = (*p)
*p = r
'''
if __name__ == '__main__':
    log('hello')
