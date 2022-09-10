# https://www.hackerrank.com/challenges/merge-two-sorted-linked-lists/problem
# O(N)

import sys

class SinglyLinkedListNode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class SinglyLinkedList(object):
    def __init__(self):
        self.head = None

    def insert_node(self, node_data):
        new_node = SinglyLinkedListNode(node_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

def mergeLists(l1, l2):
    curr1 = l1
    curr2 = l2
    l3 = SinglyLinkedList()

    if curr1.data <= curr2.data:
        l3 = curr1
        curr1 = curr1.next
    else:
        l3 = curr2
        curr2 = curr2.next

    curr3 = l3
    while curr1 is not None or curr2 is not None:
        if curr1 is None:
            curr3.next = curr2
            break;
        elif curr2 is None:
            curr3.next = curr1
            break;
        else:
            if curr1.data <= curr2.data:
                curr3.next = curr1
                curr1 = curr1.next
            else:
                curr3.next = curr2
                curr2 = curr2.next
            curr3 = curr3.next
    return l3

def print_singly_linked_list(list, delim):
    curr = list
    while curr is not None:
        print(str(curr.data) + str(delim), end='')
        curr = curr.next

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    tests = int(input())

    for tests_itr in range(tests):
        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)

        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)

        llist3 = mergeLists(llist1.head, llist2.head)

        print_singly_linked_list(llist3, ' ')
        fptr.write('\n')

    fptr.close()
