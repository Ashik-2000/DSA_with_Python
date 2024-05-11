class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


node1 = Node(3)
node2 = Node(5)
node3 = Node(13)
node4 = Node(2)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node1

node1.prev = node4
node2.prev = node1
node3.prev = node2
node4.prev = node3

firstnode = node1
lastnode = node4

print("\nForward Traversing: ")
currentnode = node1
print(currentnode.data, end=' -> ')
currentnode = currentnode.next
while currentnode != firstnode:
    print(currentnode.data, end=' -> ')
    currentnode = currentnode.next
print("Null")


print("\n Backward Traversing: ")
currentnode = node4
print(currentnode.data, end=' -> ')
currentnode = currentnode.prev
while currentnode != lastnode:
    print(currentnode.data,end=" -> ")
    currentnode = currentnode.prev
print("Null")