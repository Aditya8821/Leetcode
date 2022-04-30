# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sol(self,root):
        if not root: return 0
        left_sum=max(self.sol(root.left),0)
        right_sum=max(self.sol(root.right),0)
        self.maxsum=max(self.maxsum,left_sum+right_sum+root.val)
        return root.val+max(left_sum,right_sum)
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxsum=float("-inf")
        self.sol(root)
        return self.maxsum