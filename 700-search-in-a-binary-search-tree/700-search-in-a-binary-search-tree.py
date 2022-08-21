# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def search(rt):
            if rt:
                if rt.val==val: return rt
                elif rt.val>val: return search(rt.left)
                else: return search(rt.right)
        return search(root)
    
        
                
    