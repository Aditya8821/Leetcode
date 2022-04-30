# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sol(self,root):
        if not root: return 0
        left_height=self.sol(root.left)
        right_height=self.sol(root.right)
        path=left_height+right_height
        if path>self.maxi:
            self.maxi=path
        return 1+max(left_height,right_height)
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxi=0
        self.sol(root)
        return self.maxi
    
            