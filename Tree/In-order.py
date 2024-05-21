#        R
#       / \
#      A   B
#     / \ / \
#    C  D E  F
#           /
#          G

class TreeNode():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Pre-Order traversal function
def inOrderTraversal(node):
    if node == None:
        return
    inOrderTraversal(node.left)
    print(node.data, end=", ")
    inOrderTraversal(node.right)


root = TreeNode('R')
nodeA = TreeNode('A')
nodeB = TreeNode('B')
nodeC = TreeNode('C')
nodeD = TreeNode('D')
nodeE = TreeNode('E')
nodeF = TreeNode('F')
nodeG = TreeNode('G')

root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeF.left = nodeG

# Traversal
inOrderTraversal(root)
