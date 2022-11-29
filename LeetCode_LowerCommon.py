# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree
# Output: integer
# Input: root
# Strategy:
# 1. DFS (backtracking) and compare stacks
# 2. [1,2,5,11]
# 3. [1,2,4,9]

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        pathp = []
        pathq = []
        inter = set()
        maxCommon = 0
        if self.getPath(root, pathp, p) and self.getPath(root, pathq, q):
            inter = set(pathp).intersection(set(pathq))
        if len(inter) == 1:
            return inter.pop()
        else:
            while inter:
                i = inter.pop()
                if i.val > maxCommon:
                    maxCommon = i
            return maxCommon

    def getPath(self, root, path, k):
        path.append(root)
        if root.val == k:
            return True
        if not root.left and not root.right:
            path.pop()
            return False

        if self.getPath(root.left, path, k) or self.getPath(root.right, path, k):
            return True

        path.pop()
        return False


so = Solution()

# tree = TreeNode(1)
# tree.left = TreeNode(2)
# tree.right = TreeNode(3)
# tree.left.left = TreeNode(4)
# tree.left.right = TreeNode(5)
# tree.left.left.left = TreeNode(8)
# tree.left.left.right = TreeNode(9)
# tree.left.right.left = TreeNode(10)
# tree.left.right.right = TreeNode(11)
# tree.right.left = TreeNode(6)
# tree.right.right = TreeNode(7)
# tree.right.left.left = TreeNode(12)
# tree.right.left.right = TreeNode(13)
# tree.right.right.left = TreeNode(14)
# tree.right.right.right = TreeNode(15)
#
# print(so.lowestCommonAncestor(tree, 9, 11))

tree1 = TreeNode(3)
tree1.left = TreeNode(5)
tree1.right = TreeNode(1)
tree1.left.left = TreeNode(6)
tree1.left.right = TreeNode(2)
tree1.left.right.left = TreeNode(7)
tree1.left.right.right = TreeNode(4)
tree1.left.left.left = None
tree1.left.left.right = None
tree1.right.left = TreeNode(0)
tree1.right.right = TreeNode(8)

print(so.lowestCommonAncestor(tree1, 5, 1))
