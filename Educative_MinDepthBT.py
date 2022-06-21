# https://www.educative.io/answers/how-to-find-the-minimum-depth-of-a-binary-tree
import sys

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def minDepth(node, minDep):
    if node is None:
        return sys.maxsize
    L = minDepth(node.left, minDep)
    R = minDepth(node.right, minDep)
    if L == sys.maxsize and R == sys.maxsize: #LEAF
        tempDep = 1
    else:
        tempDep = min(L,R) + 1
    minDep = tempDep
        #min(L, R, tempDep)
    return minDep

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(7)
    root.right.right = Node(6)
    root.right.left = Node(8)
    print(minDepth(root, sys.maxsize))