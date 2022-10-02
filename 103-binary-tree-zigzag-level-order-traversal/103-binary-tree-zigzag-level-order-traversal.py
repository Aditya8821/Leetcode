# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        queue=[[root]]
        res=[]
        flag=0
        while queue:
            level=queue.pop()
            res.append(item.val for item in level)
            nxtlevel=[]
            if flag==0:
                for node in level[::-1]:
                    if node.right:
                        nxtlevel.append(node.right)
                    if node.left:
                        nxtlevel.append(node.left)
                flag=1
            else:
                for node in level[::-1]:
                    if node.left:
                        nxtlevel.append(node.left)
                    if node.right:
                        nxtlevel.append(node.right)
                flag=0
            if nxtlevel:
                queue.append(nxtlevel)
        return res
        
        