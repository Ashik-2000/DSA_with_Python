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


def search(node, target):
    if node is  None:
        return False
    elif node.data == target:
        return True
    elif target < node.data:
        return search(node.left, target)
    else:
        return search(node.right, target)


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

print(search(root, 15))