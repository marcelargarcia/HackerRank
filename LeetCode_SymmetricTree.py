# https://leetcode.com/problems/symmetric-tree
from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# DFS - Recursive
class Solution(object):
    def isSymmetric(self, root):
        return self.helper(root.left, root.right)

    def helper(self, root1, root2):
        if root1 is None and root2 is not None:
            return False
        if root1 is not None and root2 is None:
            return False
        if root1 is None and root2 is None:
            return True
        if root1.val != root2.val:
            return False
        return self.helper(root1.left, root2.right) and \
               self.helper(root1.right, root2.left)


# BFS - Iterative
class SolutionBFS(object):
    def isSymmetric(self, root):
        to_visit = deque()
        visited = set()
        if root:
            to_visit.append(root)
        while to_visit:
            if set(to_visit) == {'None'}:
                return True
            inLevel = len(to_visit)
            tamLevel = inLevel
            inLevelStack = []
            while inLevel:
                elem = to_visit.popleft()
                if not inLevelStack or (len(inLevelStack) < tamLevel / 2 and inLevel >= tamLevel / 2):
                    if elem == 'None':
                        inLevelStack.append('None')
                        visited.add(elem)
                        inLevel -= 1
                        continue
                    else:
                        inLevelStack.append(elem.val)
                else:
                    if elem == 'None':
                        if inLevelStack[-1] == elem:
                            inLevelStack.pop()
                            visited.add(elem)
                            inLevel -= 1
                            continue
                        else:
                            return False
                    else:
                        if inLevelStack[-1] == elem.val:
                            inLevelStack.pop()
                        else:
                            return False

                if elem.left and elem.left not in visited:
                    to_visit.append(elem.left)
                if not elem.left:
                    to_visit.append('None')
                if elem.right and elem.right not in visited:
                    to_visit.append(elem.right)
                if not elem.right:
                    to_visit.append('None')

                visited.add(elem)
                inLevel -= 1
        return True

so = Solution()

tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(2)
tree.left.left = TreeNode(3)
tree.left.right = TreeNode(4)
tree.right.right = TreeNode(3)
tree.right.left = TreeNode(4)

print(so.isSymmetric(tree))


tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(2)
tree.left.right = TreeNode(3)
tree.right.right = TreeNode(3)

print(so.isSymmetric(tree))
