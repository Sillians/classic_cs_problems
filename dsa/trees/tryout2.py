# from tree import Node

class TreeNode:
    def __init__(self, data, left: int = None, right: int = None) -> None:
        self.data = data
        self.left = left
        self.right = right

def sum_values(root):
    if (root == None):
        return 0
    return root.data + sum_values(root.left) + sum_values(root.right)


# Sum the sample tree
#  Our example tree looks like this:
#        15
#      /    \
#    10      20
#  /   \    /  \ 
# 8    12  16  25

# In the above binary tree sum = 106. 
# The idea is to recursively, call left subtree sum, right subtree sum and add their values to current node’s data. 


# Driver Code 
if __name__ == '__main__':
    root = TreeNode(15) 
    root.left = TreeNode(10) 
    root.right = TreeNode(20) 
    root.left.left = TreeNode(8) 
    root.left.right = TreeNode(12) 
    root.right.left = TreeNode(16) 
    root.right.right = TreeNode(25) 
 
    sum = sum_values(root) 
 
    print("Sum of all the nodes is:", sum)