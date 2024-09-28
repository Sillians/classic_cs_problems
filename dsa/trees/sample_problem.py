# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
        
# def sum_values(root):
#     if (root == None):
#         return 0
#     right_sum = root.data + sum_values(root.right) + sum_values(root.left)
#     left_sum = root.data + sum_values(root.left)  + sum_values(root.right)
    
#     if right_sum > left_sum:
#         return "Right"
#     return "Left"


# #  Our example tree looks like this:
# #         3
# #       /   \
# #      6     2
# #     /     /
# #    9     10


# node2 = Node(3)
# node3 = Node(6)
# node4 = Node(2)
# node5 = Node(9)
# node6 = Node(10)

# node2.left = node3
# node2.right = node4
# node3.left = node5
# node4.left = node6

# # print("Sum of all values of this tree is (should print 20):")
# print(sum_values(node2))
    
