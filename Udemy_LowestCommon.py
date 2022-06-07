# https://www.udemy.com/course/11-essential-coding-interview-questions
# O(
# No duplicates, BT
from collections import deque


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)

def lca(root, j, k):
    path_j = []
    path_k = []
    if hasPath(path_j, root, j) and hasPath(path_k, root, k):
        path_j.extend(path_k)
        common = []
        for c in path_j:
            if path_j.count(c) > 1:
                common.append(c)
        return common.pop()
    return None



#DFS
def hasPath(path, node, x):
    if node is None:
        return False
    if node.value == x:
        path.append(node) #O(1)
        return True
    path.append(node) #O(1)

    if (hasPath(path, node.left, x) or hasPath(path, node.right, x)):
        return True
    else:
        path.remove(node) #O(n)
        return False

#  head2 = 5
#        /   \
#       1     4
#      /\    / \
#     3  8  9  2
#    /\
#   6  7

def is_leaf(node):
    if node.left is None and node.right is None:
        return True
    else:
        return False


def create_tree(mapping, head_value):
    head = Node(head_value)
    nodes = {head_value: head}
    for key, value in mapping.items():
        nodes[value[0]] = Node(value[0])
        nodes[value[1]] = Node(value[1])
    for key, value in mapping.items():
        nodes[key].left = nodes[value[0]]
        nodes[key].right = nodes[value[1]]
    return head


# NOTE: The following values will be used for testing your solution.

# The mapping we're going to use for constructing a tree.
# {0: [1, 2]} means that 0's left child is 1, and its right
# child is 2.
mapping1 = {0: [1, 2], 1: [3, 4], 2: [5, 6]}
head1 = create_tree(mapping1, 0)
# This tree is:
# head1 = 0
#        / \
#       1   2
#      /\   /\
#     3  4 5  6

mapping2 = {5: [1, 4], 1: [3, 8], 4: [9, 2], 3: [6, 7]}
head2 = create_tree(mapping2, 5)
# This tree is:
#  head2 = 5
#        /   \
#       1     4
#      /\    / \
#     3  8  9  2
#    /\
#   6  7


print(lca(head1, 1, 5))
# should return 0
print(lca(head1, 3, 1))
# should return 1
print(lca(head1, 1, 4))
# should return 1
print(lca(head1, 0, 5))
# should return 0
print(lca(head2, 4, 7))
# should return 5
print(lca(head2, 3, 3))
# should return 3
print(lca(head2, 8, 7))
# should return 1
print(lca(head2, 3, 0))
# should return None (0 does not exist in the tree)
