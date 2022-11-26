#https://leetcode.com/problems/binary-tree-level-order-traversal

from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root):
    to_visit = deque()
    visited = set()
    res = []
    if root:
        to_visit.append(root)

    while to_visit:
        q = len(to_visit)
        level = []

        while q:
            elem = to_visit.popleft()
            visited.add(elem)
            level.append(elem.val)

            if elem.left and elem.left not in visited:
                to_visit.append(elem.left)
            if elem.right and elem.right not in visited:
                to_visit.append(elem.right)
            q -=1

        res.append(level)

    return res


tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(4)
tree.right.right = TreeNode(5)
print(levelOrder(tree))
#print(levelOrder([]))