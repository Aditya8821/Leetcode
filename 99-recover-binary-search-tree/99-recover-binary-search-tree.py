# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self,root):
        if not root:
            return
        self.inorder(root.left)
        if self.prevnode:
            if self.prevnode.val>root.val:
                if not self.first:
                    self.first=self.prevnode
                self.second=root
        self.prevnode=root
        self.inorder(root.right)
        
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.first,self.second,self.prevnode=None,None,None
        self.inorder(root)
        self.first.val,self.second.val=self.second.val,self.first.val
        
    