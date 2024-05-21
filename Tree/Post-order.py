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
def postOrderTraversal(node):
    if node == None:
        return
    postOrderTraversal(node.left)
    postOrderTraversal(node.right)
    print(node.data, end=", ")


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
postOrderTraversal(root)
