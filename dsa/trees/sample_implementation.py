# Python3 Program to print sum of all
# the elements of a binary tree

# Binary Tree Node
class NewNode:

	# Utility function to create a new node
	def __init__(self, key, left: int = None, right: int = None) -> int:
		self.key = key
		self.left = left
		self.right = right

# Function to find sum of all the element
def sumBT(root):
	# sum variable to track the sum of
	# all variables.
	sum_ = 0

	q = []

	# Pushing the first level.
	q.append(root)

	# Pushing elements at each level from
	# the tree.
	while len(q) > 0:
		temp = q.pop(0)

		# After popping each element from queue
		# add its data to the sum variable.
		sum_ += temp.key

		if (temp.left != None):
			q.append(temp.left)
		if temp.right != None:
			q.append(temp.right)

	return sum_

# Sum the sample tree
#  Our example tree looks like this:
#        15
#      /    \
#    10      20
#  /   \    /  \ 
# 8    12  16  25
#     /     \    \
#    7      13    9 
#


# Driver Code
if __name__ == '__main__':
    root = NewNode(15)
    root.left = NewNode(10)
    root.right = NewNode(20)
    root.left.left = NewNode(8)
    root.left.right = NewNode(12)
    root.left.right.left = NewNode(7)
    root.right.left = NewNode(16)
    root.right.right = NewNode(25)
    root.right.left.right = NewNode(13)
    root.right.right.right = NewNode(9)
    
    print("Sum of all elements in the binary tree is: ", sumBT(root))


