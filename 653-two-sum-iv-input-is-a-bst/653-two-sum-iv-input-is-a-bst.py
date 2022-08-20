# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. In this approach we have initated a queue with the root node and created a set 's' which will store all the values in it.
# 2. Then we will extract the root node by popping it from the queue and sustract it's value from target value to retrieve the remaining value, and if that remaining value is present there in the 's' the we will return True, else add that current value in the and if that current have it's left and right then adding them in the queue form further processing.///////We will repeat this 2nd point until queue becomes empty.

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        val={}
        def help(node):
            if not node:
                return False
            if k-node.val in val:
                return True
            val[node.val]=True
            return help(node.left) or help(node.right)
        return help(root)
    