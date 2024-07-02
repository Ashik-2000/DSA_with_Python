#        R
#       / \
#      A   B
#     / \ / \
#    C  D E  F
#           /
#          G
''''
The Root node will be on index 0. Now let's assume the index of a 
node is i, now the left child will be on 2*i+1 index and the right child
will be placed on 2*i+2 index.
'''
binary_tree = ['R','A','B','C','D','E','F',None,None,None,None,None,None,'G']

def leftnodeindex(parent):
    return binary_tree.index(parent)*2 + 1

def rightnodeindex(parent):
    return binary_tree.index(parent)*2 + 2

def getdata(index):
    if 0 <= index < len(binary_tree):
        return binary_tree[index]
    return None

rootright = getdata(rightnodeindex('R'))
rootright = getdata(rightnodeindex(rootright))
left_of_rootright = getdata(leftnodeindex(rootright))

print("Root.right.right.left data: ", left_of_rootright)