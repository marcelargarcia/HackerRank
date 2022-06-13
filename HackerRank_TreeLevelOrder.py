
# https://www.hackerrank.com/challenges/tree-level-order-traversal/problem
# O(n)

from collections import deque

class Node:
    def __init__(self, info, left=None, right=None):
        self.info = info
        self.left = left
        self.right = right

# O(N)
def levelOrder(root):
    arr = deque([])
    arr.append(root)

    if root is None:
        print(None)
    if not root.left and not root.right:
        print(arr[0].info)
    else:
        while arr:
            node = arr[0]
            print(str(node.info) + " ", end='')
            arr.popleft()
            if node.left:
                arr.append(node.left)
            if node.right:
                arr.append(node.right)

