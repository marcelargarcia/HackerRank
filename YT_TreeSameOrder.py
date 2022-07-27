# https://www.youtube.com/watch?v=7lbwfkCfNQ4
# "Given two Binary Trees, determine whether they have the same inorder/preorder/posorder transversal"

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


#################### IN ORDER #################### # Esquerda, Nó, Direita. Raiz no meio de tudo. Sequencia ordenada em BST.
def sameInOrder(t1, t2):
    if printInOrder(t1) == printInOrder(t2):
        return True
    else:
        return False


def printInOrder(t):
    node = t
    printedNodes = []
    visitedStack = []
    printInOrder = []
    while node:
        visitedStack.append(node)
        if node.left is not None and node.left not in printedNodes:
            node = node.left
        else:
            printedNodes.append(visitedStack.pop())
            if node.right is not None:
                node = node.right
            elif visitedStack:
                node = visitedStack.pop()
            else:
                break
    for i in range(len(printedNodes)):
        printInOrder.append(printedNodes[i].val)
    return printInOrder


def sameInOrder_2(t1, t2):
    printInOrder_t1 = []
    printInOrder_t2 = []

    if printInOrder_2(t1, printInOrder_t1) == printInOrder_2(t2, printInOrder_t2):
        return True
    else:
        return False


def printInOrder_2(t, printInOrder):
    if t is None:
        return
    printInOrder_2(t.left, printInOrder)
    printInOrder.append(t.val)
    printInOrder_2(t.right, printInOrder)

    return printInOrder


#################### PRE ORDER #################### # Nó, Esquerda, Direita. Raiz no início de tudo.
def samePreOrder(t1, t2):
    if printPreOrder(t1) == printPreOrder(t2):
        return True
    else:
        return False


def printPreOrder(t):
    visitedStack = []
    printedNodes = []
    printPreOrder = []

    node = t
    while node:
        visitedStack.append(node)
        if node not in printedNodes:
            printedNodes.append(node)

        if node in visitedStack and (
                ((node.left and node.left in printedNodes) or not node.left) and
                ((node.right and node.right in printedNodes) or not node.right)):
            visitedStack.pop()
        if node.left and node.left not in printedNodes:
            node = node.left
        elif node.right and node.right not in printedNodes:
            node = node.right
        elif visitedStack:
            node = visitedStack.pop()
        else:
            break

    for i in range(len(printedNodes)):
        printPreOrder.append(printedNodes[i].val)
    return printPreOrder

def samePreOrder_2(t1, t2):
    printPreOrder_t1 = []
    printPreOrder_t2 = []

    if printPreOrder_2(t1, printPreOrder_t1) == printPreOrder_2(t2, printPreOrder_t2):
        return True
    else:
        return False


def printPreOrder_2(t, printPreOrder):
    if t is None:
        return
    printPreOrder.append(t.val)
    printPreOrder_2(t.left, printPreOrder)
    printPreOrder_2(t.right, printPreOrder)

    return printPreOrder

#################### POST ORDER #################### # Esquerda, Direita, Nó. Raiz no fim de tudo.
def samePostOrder(t1, t2):
    if printPostOrder(t1) == printPostOrder(t2):
        return True
    else:
        return False


def printPostOrder(t):
    visitedStack = []
    printedNodes = []
    printPostOrder = []

    node = t
    while node:
        visitedStack.append(node)
        if (not node.left or node.left in printedNodes) and (not node.right or node.right in printedNodes):
            printedNodes.append(visitedStack.pop())
        if node.left and node.left not in printedNodes:
            node = node.left
        elif node.right and node.right not in printedNodes:
            node = node.right
        elif visitedStack:
            node = visitedStack.pop()
        else:
            break

    for i in range(len(printedNodes)):
        printPostOrder.append(printedNodes[i].val)
    return printPostOrder

def samePostOrder_2(t1, t2):
    printPostOrder_t1 = []
    printPostOrder_t2 = []

    if printPostOrder_2(t1, printPostOrder_t1) == printPostOrder_2(t2, printPostOrder_t2):
        return True
    else:
        return False


def printPostOrder_2(t, printPostOrder):
    if t is None:
        return
    printPostOrder_2(t.left, printPostOrder)
    printPostOrder_2(t.right, printPostOrder)
    printPostOrder.append(t.val)

    return printPostOrder

if __name__ == '__main__':
    t1 = Node(5)
    t1.left = Node(3)
    t1.right = Node(7)
    t1.left.left = Node(1)
    t1.right.left = Node(6)

    t2 = Node(3)
    t2.left = Node(1)
    t2.right = Node(6)
    t2.right.left = Node(5)
    t2.right.right = Node(7)

    # print(sameInOrder(t1, t2))
    print(sameInOrder_2(t1, t2))
    # print(samePreOrder(t1, t2))
    print(samePreOrder_2(t1, t2))
    # print(samePostOrder(t1, t2))
    print(samePostOrder_2(t1,t2))
    print("teste")