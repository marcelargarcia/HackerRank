# https://leetcode.com/problems/diameter-of-binary-tree/

import sys
from collections import deque

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def diameterOfBinaryTree(node, diam):
    if node is None:
        return 0

    L = diameterOfBinaryTree(node.left, diam)
    R = diameterOfBinaryTree(node.right, diam)

    diam = max(diam + 1, L + R)
    return diam


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print(diameterOfBinaryTree(root, 0))

    root2 = Node(1)
    root2.left = Node(2)
    print(diameterOfBinaryTree(root2, 0))


