# Use this class to create binary trees.
import sys


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)


# DFS
def is_bst(node, lower_lim=None, upper_lim=None):
    if node is None:
        return True
    else:
        if upper_lim is None: upper_lim = sys.maxsize
        if lower_lim is None: lower_lim = -sys.maxsize - 1

        if upper_lim > node.value > lower_lim:
            bst = True
        else:
            bst = False

        if bst:
            bst_left = is_bst(node.left, lower_lim, node.value)
        else:
            bst_left = False

        if bst_left and bst:
            bst_right = is_bst(node.right, node.value, upper_lim)
        else:
            bst_right = False

    return bst and bst_left and bst_right


#  head1 = 0
#        /   \
#       1     2
#      /\    / \
#     3  4  5   6


# A function for creating a tree.
# Input:
# - mapping: a node-to-node mapping that shows how the tree should be constructed
# - head_value: the value that will be used for the head ndoe
# Output:
# - The head node of the resulting tree
def create_tree(mapping, head_value):
    nodes = {head_value: Node(head_value)}

    for k, v in mapping.items():
        nodes[v[0]] = Node(v[0])
        nodes[v[1]] = Node(v[1])

    for k, v in mapping.items():
        d = nodes.get(k)
        cl = nodes.get(v[0])
        cr = nodes.get(v[1])
        d.left = cl
        d.right = cr

    return nodes.get(head_value)


# NOTE: The following values will be used for testing your solution.

# The mapping we're going to use for constructing a tree.
# {0: [1, 2]} means that 0's left child is 1, and its right
# child is 2.
mapping0 = {0: [1, 2]}
mapping1 = {0: [1, 2], 1: [3, 4], 2: [5, 6]}
mapping2 = {3: [1, 4], 1: [0, 2], 4: [5, 6]}
mapping3 = {3: [1, 5], 1: [0, 2], 5: [4, 6]}
mapping4 = {3: [1, 5], 1: [0, 4]}
head0 = create_tree(mapping0, 0)
# This tree is:
#  head0 = 0
#        /   \
#       1     2
head1 = create_tree(mapping1, 0)
# This tree is:
#  head1 = 0
#        /   \
#       1     2
#      /\    / \
#     3  4  5   6
head2 = create_tree(mapping2, 3)
# This tree is:
#  head2 = 3
#        /   \
#       1     4
#      /\    / \
#     0  2  5   6
head3 = create_tree(mapping3, 3)
# This tree is:
#  head3 = 3
#        /   \
#       1     5
#      /\    / \
#     0  2  4   6
head4 = create_tree(mapping4, 3)
# This tree is:
#  head4 = 3
#        /   \
#       1     5
#      /\
#     0  4

print(is_bst(head0))
# should return False
print(is_bst(head1))
# should return False
print(is_bst(head2))
# should return False
print(is_bst(head3))
# should return True
print(is_bst(head4))
# should return False
