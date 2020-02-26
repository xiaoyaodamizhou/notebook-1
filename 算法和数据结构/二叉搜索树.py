def log(*args, **kwargs):
    print(*args, **kwargs)

'''
二叉搜索树实现（BST）
二叉搜索的中序遍历
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None


class BST:
    def __init__(self, node_list):
        self.root = Node(node_list[0])
        self.logging = []
        for data in node_list[1:]:
            self.insert(data)

    # 搜索
    def search(self, node, parent, data):
        if node is None:
            return False, node, parent
        if node.data == data:
            return True, node, parent
        if node.data > data:
            return self.search(node.lchild, node, data)
        else:
            return self.search(node.rchild, node, data)

    # 插入
    def insert(self, data):
        flag, n, p = self.search(self.root, self.root, data)
        if not flag:
            new_node = Node(data)
            if data > p.data:
                p.rchild = new_node
            else:
                p.lchild = new_node

    # 删除
    # 删除节点是叶子节点，直接删除不影响树的结构

    # 删除节点只有左子树或只有右子树，删除节点后
    # 将他的左子树或右子树的整个移动到删除节点的位置即可

    # 删除既有左子树又有右子树的节点，找到要删除节点p的直接前驱
    # 或者直接后继s，用s来替换节点p,然后再删除此节点s
    def delete(self, root, data):
        flag, n, p = self.search(root, root, data)
        if flag is False:
            log('找不到')
        else:
            if n.lchild is None:
                if n == p.lchild:
                    p.lchild = n.rchild
                if p.rchild == n:
                    p.rchild = n.rchild
                if n == self.root:
                    self.root = n.rchild
                del n
            elif n.rchild is None:
                if n == p.lchild:
                    p.lchild = n.lchild
                if n == p.rchild:
                    p.rchild = n.lchild
                if n == self.root:
                    self.root = n.lchild
                del n
            else:
                pre = n.rchild
                if pre.lchild is None:
                    n.data = pre.data
                    n.rchild = pre.rchild
                    del pre
                else:
                    next = pre.lchild
                    while next.lchild is not None:
                        pre = next
                        next = next.lchild
                    n.data = next.data
                    pre.lchild = next.rchild
                    del next

    def inOrderTraverse(self, node):
        if node is None:
            return []
        else:
            res = []
            left = self.inOrderTraverse(node.lchild)
            res.append(node.data)
            right = self.inOrderTraverse(node.rchild)
        return left + res + right


# 有序数组转化成搜索二叉树
def sortedArrayToBST(nums):
    if nums:
        midPos = len(nums) // 2
        mid = nums[midPos]
        root = Node(mid)
        root.lchild = sortedArrayToBST(nums[:midPos])
        root.rchild = sortedArrayToBST(nums[midPos + 1:])
        return root


def test():
    node_list = [1, 2, 3, 4, 5, 6, 7, 8]
    bst = BST(node_list)
    bst.delete(bst.root, 1)
    log(bst.inOrderTraverse(bst.root))
    bst.delete(bst.root, 7)
    log(bst.inOrderTraverse(bst.root))
    bst.delete(bst.root, 8)
    log(bst.inOrderTraverse(bst.root))


if __name__ == '__main__':
    test()