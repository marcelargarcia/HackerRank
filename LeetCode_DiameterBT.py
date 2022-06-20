# https://leetcode.com/problems/diameter-of-binary-tree/
# Definition for a binary tree node.

import sys
from collections import deque

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def diameterOfBinaryTree(root):
    return 0



def calcPath(self, node1, node2):

    return 0

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print(diameterOfBinaryTree(root))



