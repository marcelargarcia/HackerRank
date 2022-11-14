# https://leetcode.com/problems/find-duplicate-subtrees/description/

from collections import deque
class Node():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#SOLUTION 1:
def findDuplicateSubtrees(root):
    hmap = {}
    res = []
    def subTree(node, path):
        if node is None:
            return '#'
        path += ','.join([str(node.val), subTree(node.left, path), subTree(node.right, path)])

        if path in hmap:
            hmap[path] += 1
            if hmap[path] == 2:
                # path_list = list(map(int,path.replace(',#', '').split(',')))
                res.append(node)
        else:
            hmap[path] = 1
        return path

    subTree(root, '')
    return res



#SOLUTION 2:
def findDuplicateSubtrees_2(self, root):
    hmap = {}
    to_check = deque([])
    to_check.append(root)
    checked = []
    res = []
    while to_check:
        cur = to_check.popleft()
        if cur.left and cur.left not in checked:
            to_check.append(cur.left)
        if cur.right and cur.right not in checked:
            to_check.append(cur.right)
        path = self.subTree(cur, '')
        if path in hmap:
            hmap[path] += 1
            if hmap[path] == 2:
                # path_list = list(map(int,path.replace(',#', '').split(',')))
                res.append(cur)
        else:
            hmap[path] = 1

        checked.append(cur)

    return res

def subTree_2(self, node, path):
    if node is None:
        return '#'
    path += ','.join([str(node.val), self.subTree(node.left, path), self.subTree(node.right, path)])

    return path


####################################

root = Node(2)
root.left = Node(2)
root.left.left = Node(3)
root.right = Node(2)
root.right.left = Node(3)
print(findDuplicateSubtrees(root))


root1 = Node(2)
root1.left = Node(1)
root1.right = Node(1)
print(findDuplicateSubtrees(root1))

root2 = Node(1)
root2.left = Node(2)
root2.left.left = Node(4)
root2.right = Node(3)
root2.right.left = Node(2)
root2.right.right = Node(4)
root2.right.left.left = Node(4)
print(findDuplicateSubtrees(root2))