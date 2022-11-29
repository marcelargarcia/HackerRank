#https://leetcode.com/problems/path-sum/

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def hasPathSum(self, root, targetSum):
        if not root:
            return False
        if not root.left and not root.right and targetSum == root.val:
            return True

        return self.hasPathSum(root.left, (targetSum - root.val)) \
               or self.hasPathSum(root.right, (targetSum - root.val))

so = Solution()

tree = TreeNode(5)
tree.left = TreeNode(4)
tree.left.left = TreeNode(11)
tree.left.left.left = TreeNode(7)
tree.left.left.right = TreeNode(2)
tree.right = TreeNode(8)
tree.right.left = TreeNode(13)
tree.right.right = TreeNode(4)
tree.right.right.right = TreeNode(1)
print(so.hasPathSum(tree, 22))

tree1 = TreeNode(1)
tree1.left = TreeNode(2)
tree1.right = TreeNode(3)

print(so.hasPathSum(tree1, 5))
print(so.hasPathSum(tree1, 4))

print(so.hasPathSum(None, 0))