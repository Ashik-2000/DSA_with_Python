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

# Insertion function
def insert(node, data):
    if node is None:
        return Treenode(data)
    else:
        if data < node.data:
            node.left = insert(node.left, data)
        elif data > node.data:
            node.right = insert(node.right, data)
    return node

# In-Order traversal function
def inOrderTraversal(node):
    if node == None:
        return
    inOrderTraversal(node.left)
    print(node.data, end=", ")
    inOrderTraversal(node.right)


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

insert(root, 17)
inOrderTraversal(root)