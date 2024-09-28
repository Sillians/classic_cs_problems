class TreeNode:
    def __init__(self, data, left: int = None, right: int = None) -> None:
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
            
    def solve(self, root) -> int:
        if not root:
            return 0
        return self.recurse(root)
    
#  Our example tree looks like this:
#      2
#       \
#        4
#       /  \ 
#      3    5

ob = Solution()
root = TreeNode(2)
root.right = TreeNode(4)
root.right.left = TreeNode(3)
root.right.right = TreeNode(5)
print(ob.solve(root))
        