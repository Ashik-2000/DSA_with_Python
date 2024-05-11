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


def deleteanode(first, deletenode):
    if first == deletenode:
        return first.next
    
    currentnode = first
    recentnode = None
    while currentnode:
        if currentnode == deletenode:
            recentnode.next = currentnode.next
        if currentnode is None:
            return first
        recentnode = currentnode
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

print("Before delet:")
traversenode(node1)

print("After delete:")
node1 = deleteanode(node1, node4)
traversenode(node1)
