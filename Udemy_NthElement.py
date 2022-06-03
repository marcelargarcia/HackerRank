# https://www.udemy.com/course/11-essential-coding-interview-questions
# O(N)


# Use this class to create linked lists.
class Node:
    def __init__(self, value, last=None, next=None):
        self.value = value
        self.last = last
        self.next = next

    # The string representation of this node.
    # Will be used for testing.
    def __str__(self):
        return str(self.value)


# Implement your function below.
#(2N)
def nth_from_last_1(head, n):
    curr = head
    if isinstance(curr, type(None)):
        return None
    else:
        while curr.next is not None:
            curr = curr.next
        for i in range(n, 1, -1):
            curr = curr.last
        if isinstance(curr, type(None)):
            return None
        else:
            return curr

#(N)
def nth_from_last(head, n):
    curr = head
    point = head
    dist = 0
    if isinstance(curr, type(None)):
        return None
    else:
        while curr is not None:
            dist = dist + 1
            curr = curr.next
            if dist > n:
                point = point.next

        if dist < n:
            return None
        else:
            return point

# NOTE: Feel free to use the following function for testing.
# It converts the given linked list into an easy-to-read string format.
# Example: 7 -> 6 -> 5 -> 4 -> 3 -> 2 -> 1 -> (None)
def linked_list_to_string(head):
    current = head
    str_list = []
    while current:
        str_list.append(str(current.value))
        current = current.next
    str_list.append('(None)')
    print(' -> '.join(str_list))


# NOTE: The following input values will be used for testing your solution.
current = Node(1)
for i in range(2, 8):
    next = current
    current = Node(i, None, next)
    next.last = current
head = current
# linked_list_to_string(head)
# head = 7 -> 6 -> 5 -> 4 -> 3 -> 2 -> 1 -> (None)

current2 = Node(4)
for i in range(3, 0, -1):
    next2 = current2
    current2 = Node(i, None, current2)
    next2.last = current2
head2 = current2
# head2 = 1 -> 2 -> 3 -> 4 -> (None)

print(nth_from_last(head, 1))
# should return 1.
print(nth_from_last(head, 5))
# should return 5.
print(nth_from_last(head2, 2))
# should return 3.
print(nth_from_last(head2, 4))
# should return 1.
print(nth_from_last(head2, 5))
# should return None.
print(nth_from_last(None, 1))
# should return None.
