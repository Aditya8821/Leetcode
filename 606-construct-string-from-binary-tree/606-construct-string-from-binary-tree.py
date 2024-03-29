# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        res = ""
        left = self.tree2str(root.left)
        right = self.tree2str(root.right)
        if left or right:
            res += "(%s)" % left
        if right:
            res += "(%s)" % right
        return str(root.val) + res