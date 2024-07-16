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

def minvalue(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def maxvalue(node):
    current = node
    while current.right is not None:
        current = current.right
    return current

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

print(minvalue(root).data)
print(maxvalue(root).data)