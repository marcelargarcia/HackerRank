# Source: https://www.youtube.com/watch?v=7HgsS8bRvjo

# Problem: "Find Number of Universal Value Trees in a Binary Tree"

# Example:
#  A universal value tree is a subtree in each left, root and right nodes
#  contain the same value
#   3      -> is universal value tree
# 3   3
#   1      -> isn't universal value tree
# 3   3

# Questions:
# 1. Is a null tree a universal value tree? Yes

from collections import deque

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)


# BFS
# O(N)
def UniversalValueTree_BFS(root):
    children = deque([])
    summ = 0
    children.append(root)

    while children:
        node = children[0]

        if node is None or (node.left is None and node.right is None):
            summ = summ + 1

        if node and node.right:
            children.append(node.right)
        if node and node.left:
            children.append(node.left)

        if (node and node.right and node.left) and (node.value == node.right.value and node.value == node.left.value):
            summ = summ + 1

        children.popleft()
    return summ


# DFS
# O(N)
# O(log(N)) space (recursion)
def UniversalValueTree_DFS(node, summ):
    if node is None or (not node.left and not node.right):
        summ[0] = summ[0] + 1
        return True

    else:
        if not node.left:
            uvt = False
            uvt_right = UniversalValueTree_DFS(node.right, summ)

        elif not node.right:
            uvt = False
            uvt_left = UniversalValueTree_DFS(node.left, summ)

        else:  # node.left and node.right:
            if node.value == node.left.value and node.value == node.right.value:
                uvt = True
            else:
                uvt = False

            uvt_left = UniversalValueTree_DFS(node.left, summ)
            uvt_right = UniversalValueTree_DFS(node.right, summ)

            if uvt and uvt_left and uvt_right:
                summ[0] = summ[0] + 1

        return uvt and uvt_left and uvt_right

    return False


if __name__ == '__main__':
    root = Node(0)
    root.left = Node(1)
    root.right = Node(0)
    root.right.left = Node(1)
    root.right.right = Node(0)
    root.right.left.left = Node(1)
    root.right.left.right = Node(1)
    summ = [0]
    UniversalValueTree_DFS(root, summ)
    print("DFS:" + str(summ[0]))  # should return 5
    print("BFS:" + str(UniversalValueTree_BFS(root)))  # should return 5


    root1 = Node(3)
    root1.left = Node(3)
    root1.right = Node(3)
    summ1 = [0]
    UniversalValueTree_DFS(root1, summ1)
    print("DFS:" + str(summ1[0]))  # should return 3
    print("BFS:" + str(UniversalValueTree_BFS(root1)))

    root2 = Node(1)
    root2.left = Node(1)
    root2.right = Node(2)
    summ2 = [0]
    UniversalValueTree_DFS(root2, summ2)
    print("DFS:" + str(summ2[0]))  # should return 2
    print("BFS:" + str(UniversalValueTree_BFS(root2)))

    root3 = None
    summ3 = [0]
    UniversalValueTree_DFS(root3, summ3)
    print("DFS:" + str(summ3[0]))  # should return 1
    print("BFS:" + str(UniversalValueTree_BFS(root3)))

    root4 = Node(3)
    root4.left = Node(2)
    root4.right = Node(3)
    root4.right.right = Node(2)
    root4.right.right.left = Node(2)
    root4.right.right.right = Node(2)
    summ4 = [0]
    UniversalValueTree_DFS(root4, summ4)
    print("DFS:" + str(summ4[0]))  # should return
    print("BFS:" + str(UniversalValueTree_BFS(root4)))