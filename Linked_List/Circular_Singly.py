class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


node1 = Node(3)
node2 = Node(5)
node3 = Node(13)
node4 = Node(2)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node1

currentnode = node1
firstnode = node1
print(currentnode.data, end=' -> ')
currentnode = currentnode.next

while currentnode != firstnode:
    print(currentnode.data, end=' -> ')
    currentnode = currentnode.next
print("Null")