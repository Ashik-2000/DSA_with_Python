#         13
#        /   \
#       /     \
#      7      15
#     / \    /  \
#    3   8  14  19
#              /
#             18

class Treenode():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def minValue(node):
    current = node
    while node.left is not None:
        current = current.left
    return current

def inOrderTraversal(node):
    if node is None:
        return
    inOrderTraversal(node.left)
    print(node.data, end=' ')
    inOrderTraversal(node.right)

def delete(node, data):
    if node is None:
        return None
    if data < node.data:
        node.left = delete(node.left, data)
    elif data > node.data:
        node.right = delete(node.right, data)
    else:
        if node.left is None:
            temp = node.right
            node = None
            return temp
        elif node.right is None:
            temp = node.left
            node = None
            return temp
        node.data = minValue(node.right).data
        node.right = delete(node.right, node.data)
    return node

root = Treenode(13)
node7 = Treenode(7)
node3 = Treenode(3)
node8 = Treenode(8)
node15 = Treenode(15)
node14 = Treenode(14)
node19 = Treenode(19)
node18 = Treenode(18)

root.left = node7
root.right = node15

node7.left = node3
node7.right = node8

node15.left = node14
node15.right = node19

node19.left = node18


inOrderTraversal(root)
delete(root, 15)
print()
inOrderTraversal(root)