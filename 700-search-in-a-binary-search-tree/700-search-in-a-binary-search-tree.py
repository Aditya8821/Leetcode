# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def search(root_node):
            if root_node:
                if root_node.val == val: return root_node
                elif root_node.val < val: return search(root_node.right)
                return search(root_node.left)
        
        return search(root)