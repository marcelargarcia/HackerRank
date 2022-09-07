#https://leetcode.com/problems/add-two-numbers/


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#O(N)
def addTwoNumbers(l1, l2):
    num1 = ""
    num2 = ""

    while l1 is not None:
        num1 = str(l1.val) + num1
        l1 = l1.next
    while l2 is not None:
        num2 = str(l2.val) + num2
        l2 = l2.next

    sum = int(num1) + int(num2)

    previousNode = None
    l3 = None
    for k in reversed(range(len(str(sum)))):
        currNode = ListNode(int(str(sum)[k]))
        if l3 is None:
            l3 = currNode
        if previousNode is not None:
            previousNode.next = currNode
        previousNode = currNode

    return l3

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
print(addTwoNumbers(l1, l2))

l1 = ListNode(0)
l2 = ListNode(0)
print(addTwoNumbers(l1, l2))

l1 = ListNode(9)
l1.next = ListNode(9)
l1.next.next = ListNode(9)
l1.next.next.next = ListNode(9)
l1.next.next.next.next = ListNode(9)
l1.next.next.next.next.next = ListNode(9)
l1.next.next.next.next.next.next = ListNode(9)

l2 = ListNode(9)
l2.next = ListNode(9)
l2.next.next = ListNode(9)
l2.next.next.next = ListNode(9)

print(addTwoNumbers(l1, l2))


#O(N)
def addTwoNumbers_List(l1, l2):
    num1 = ""
    num2 = ""
    ans = []

    for i in reversed(range(len(l1))):
        num1 = num1 + str(l1[i])
    for j in reversed(range(len(l2))):
        num2 = num2 + str(l2[j])

    sum = int(num1) + int(num2)

    for k in reversed(range(len(str(sum)))):
        ans.append(int(str(sum)[k]))
    return ans

if __name__ == '__main__':
    print(addTwoNumbers_List([2,4,3],[5,6,4]))
    print(addTwoNumbers_List([0], [0]))
    print(addTwoNumbers_List([9,9,9,9,9,9,9], [9,9,9,9]))

