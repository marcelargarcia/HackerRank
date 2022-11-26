#https://leetcode.com/problems/binary-tree-preorder-traversal
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorderTraversal(root, order):
    if root:
        order.append(root.val)
        preorderTraversal(root.left,order)
        preorderTraversal(root.right,order)
    return order

tree = TreeNode(1)
tree.right = TreeNode(2)
tree.right.left = TreeNode(3)

print(preorderTraversal(tree,[]))