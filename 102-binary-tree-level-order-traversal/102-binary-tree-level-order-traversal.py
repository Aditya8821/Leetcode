# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue=[[root]]
        res=[]
        while queue:
            level=queue.pop()
            res.append(item.val for item in level)
            nxtlevel=[]
            for item in level:
                if item.left:
                    nxtlevel.append(item.left)
                if item.right:
                    nxtlevel.append(item.right)
            if nxtlevel:
                queue.append(nxtlevel)
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
                        
            
        
        