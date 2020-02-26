def log(*args, **kwargs):
    print(*args, **kwargs)


class TreeNode:
    def __init__(self, val=-1):
        self.val = val
        self.left = None
        self.right = None

# 关于二叉树的深度优先遍历
# 先序遍历，中序遍历，后序遍历
# 关于二叉树的广度优先遍历
# 层次遍历

'''
二叉树创建
'''
class Tree(object):
    def __init__(self):
        self.root = None
        self.myQueue = []

    def add(self, val):
        node = TreeNode(val)
        if self.root is None:
            self.root = node
            self.myQueue.append(self.root)
        else:
            tmp = self.myQueue[0]
            while True:
                if tmp.left is None:
                    tmp.left = node
                    if tmp.left.val is not None:
                        self.myQueue.append(tmp.left)
                    return
                if tmp.right is None:
                    tmp.right = node
                    if tmp.right.val is not None:
                        self.myQueue.append(tmp.right)
                    self.myQueue.pop(0)
                    return

    def middleOrder(self, root):
        if root is None:
            return []
        r = []
        left = self.middleOrder(root.left)
        r.append(root.val)
        right = self.middleOrder(root.right)
        return left + r + right

    def beforeOrder(self, root):
        if root is None:
            return []
        r = []
        r.append(root.val)
        left = self.beforeOrder(root.left)
        right = self.beforeOrder(root.right)
        return r + left + right

    def afterOrder(self, root):
        if root is None:
            return []
        r = []
        left = self.afterOrder(root.left)
        right = self.afterOrder(root.right)
        r.append(root.val)
        return left + right + r

    # 非递归的中序遍历
    def order(self, root):
        r = []
        result = []
        pos = root
        while pos is not None or len(r) > 0:
            if pos is not None:
                r.append(pos)
                pos = pos.left
            else:
                pos = r.pop()
                result.append(pos.val)
                pos = pos.right
        return result

    # 二叉树最大深度
    def bTreeDepth(self, node):
        if node is None:
            return 0
        ldepth = self.bTreeDepth(node.left)
        rdepth = self.bTreeDepth(node.right)
        return (max(ldepth, rdepth) + 1)

'''
二叉树深度(二叉树的深度遍历)
'''
def maxDepth(root):
    if not root:
        return []
    queue = [root]
    ans = [root.val]
    while queue:
        result = []
        for _ in range(0, len(queue)):
            node = queue.pop(0)
            if node.left:
                result.append(node.left.val)
                queue.append(node.left)
            if node.right:
                result.append(node.right.val)
                queue.append(node.right)
        if result:
            ans.append(result)
    return ans


# 镜像二叉树
def isSymmetric(self, node):
    def helper(root, mirror):
        if not root and not mirror:
            return True
        if root and mirror and root.val == mirror.val:
            return helper(root.left, mirror.right) and helper(root.right, mirror.left)
        return False

    return helper(node, node)


'''
[_, _, 3, _, _, _]
[_, _, 3, _, _, _]
[_, 2, 3, _, 5, _]
[1, _, 3, 4, _, 6]
'''

'''
由先序和中序生成二叉树
function TreeNode(x) {
    this.val = x;
    this.left = null;
    this.right = null;
}

function reConstructBinaryTree(pre, vin)
{
    if (pre.length === 0 || vin.length === 0) {
      return null
    }
    let root = new TreeNode(pre[0])
    let index = vin.indexOf(pre[0])
    let pre_left = pre.slice(1, index + 1)
    let pre_right = pre.slice(index + 1)
    let vin_left = vin.slice(0, index)
    let vin_right = vin.slice(index + 1)

    root.left = reConstructBinaryTree(pre_left, vin_left)
    root.right = reConstructBinaryTree(pre_right, vin_right)
    return root
}
'''
def test():
    tree = Tree()
    arr = [3, 5, None, None, 6, 7, 8]
    arr = [3, None, 5, 6, None, 7, None, 8, 9]
    for i in arr:
        tree.add(i)
    root = tree.root
    ans = maxDepth(root)
    log(ans)

if __name__ == '__main__':
    test()
