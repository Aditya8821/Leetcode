# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def help(root,minlimit,maxlimit):
            if not root: return True
            if root.val<=minlimit or root.val>=maxlimit:
                return False
            return help(root.left,minlimit,root.val) and help(root.right,root.val,maxlimit)
        return help(root,-2**31-1,2**31)            
        