#https://leetcode.com/problems/binary-tree-preorder-traversal
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    #Pre Order
    #https://leetcode.com/problems/binary-tree-preorder-traversal
    def preorderTraversal(self, root):
        res = []
        self.dfsPre(root, res)
        return res

    def dfsPre(self, root, res):
        if root:
            res.append(root.val)
            self.dfsPre(root.left, res)
            self.dfsPre(root.right, res)

    #In Order
    #https://leetcode.com/problems/binary-tree-inorder-traversal
    def inorderTraversal(self, root):
        res = []
        self.dfsIn(root, res)
        return res

    def dfsIn(self, root, res):
        if root:
            self.dfsIn(root.left, res)
            res.append(root.val)
            self.dfsIn(root.right, res)

    #Post Order
    #https://leetcode.com/problems/binary-tree-postorder-traversal
    def postorderTraversal(self, root):
        res = []
        self.dfsPost(root, res)
        return res

    def dfsPost(self, root, res):
        if root:
            self.dfsPost(root.left, res)
            self.dfsPost(root.right, res)
            res.append(root.val)


tree = TreeNode(1)
tree.right = TreeNode(2)
tree.right.left = TreeNode(3)

sol = Solution()
print(sol.preorderTraversal(tree,[]))