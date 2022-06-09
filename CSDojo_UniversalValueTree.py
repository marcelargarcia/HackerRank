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

# Complexity:
# O(N) time
# O(log(N)) space (recursion)