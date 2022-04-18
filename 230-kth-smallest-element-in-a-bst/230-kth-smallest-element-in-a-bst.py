# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # 0. base case, if a root doesn't exist, return None
        if not root:
            return None
        # 1. set up an answer array and heapify it
        answer = []
        heapq.heapify(answer)
        # 2. set up a helper function that takes in a node and heappushes the value of that node (if it exists) and then calls the helper function for the left and right brances of the node
        def helper(node):
            if node:
                heapq.heappush(answer, node.val)
                helper(node.left)
                helper(node.right)
        # 3. initialize the helper function
        helper(root)
        # 4. return the last value from the heap using the k smallest values
        return heapq.nsmallest(k, answer)[-1]