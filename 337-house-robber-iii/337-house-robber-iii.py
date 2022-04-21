# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:  
                return 0, 0
            max_l_ignore, max_l = dfs(node.left)
            max_r_ignore, max_r = dfs(node.right)
            return max_l + max_r, max(max_l + max_r, node.val + max_l_ignore + max_r_ignore)

        return dfs(root)[1]