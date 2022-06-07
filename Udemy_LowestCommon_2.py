# Use this class to create binary trees.
import sys

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)

# Implement your function below.
def lca(root, j, k):

    return None

def hasPath(path, root, k):
    


# head1 = 0
#        / \
#       1   2
#      /\   /\
#     3  4 5  6

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
