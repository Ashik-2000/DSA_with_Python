class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def traversenode(first):
    currentnode = first
    while currentnode:
        print(currentnode.data, end=' -> ')
        currentnode = currentnode.next
    print("Null")


def inserteanode(first, newnode, position):
    if position == 1:
        newnode.next = first
        return newnode
    
    currentnode = first
    pos = 1
    while currentnode:
        if pos == position-1:
            newnode.next = currentnode.next
            currentnode.next = newnode
        pos += 1
        currentnode = currentnode.next

    return first



node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print("Before insert:")
traversenode(node1)

new = Node(4)

print("After insert:")
node1 = inserteanode(node1, new, 3)
traversenode(node1)
