#https://leetcode.com/problems/maximum-depth-of-binary-tree

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)

        return max(leftDepth,rightDepth) + 1






tree = TreeNode(3)
tree.left = TreeNode(9)
tree.right = TreeNode(20)
tree.left.left = TreeNode(15)
tree.right.right = TreeNode(7)

so = Solution()
print(so.maxDepth(tree))

#Input: root (node)
#Output: integer
#Strategy: use leve-order traversal (BFS) recursively to find all depths and check if this depth is
    # the max one
#Edge cases:
    # Empty tree []
    # Tree with only 1 depth (non-balanced tree)
    #  1
    #   2
    #    5
    #     20
    #      97
