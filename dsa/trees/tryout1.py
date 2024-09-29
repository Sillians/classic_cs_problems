class TreeNode:
    def __init__(self, data, left: int = None, right: int = None):
        self.val = data
        self.left = left
        self.right = right
        
class Solution:
    def recurse(self, node) -> int:
        val = node.val
        
        if node.left:
            val += self.recurse(node.left)
        if node.right:
            val += self.recurse(node.right)
        return val
    
    def solve(self, root = None) -> int:
        if not root:
            return 0
        return self.recurse(root)


#  Our example tree looks like this:
#         3
#       /   \
#      6     2
#     /     /
#    9     10


ob = Solution()
root = TreeNode(3)
root.right = TreeNode(2)
root.left = TreeNode(6)
root.right.left = TreeNode(10)
root.left.left = TreeNode(9)
print(ob.solve(root))