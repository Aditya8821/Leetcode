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
            nextlevel=[]
            if flag==0:
                for item in level[::-1]:
                    if item.right:
                        nextlevel.append(item.right)
                    if item.left:
                        nextlevel.append(item.left)
                    flag=1
            else:
                for item in level[::-1]:
                    if item.left:
                        nextlevel.append(item.left)
                    if item.right:
                        nextlevel.append(item.right)
                    flag=0
            if nextlevel:
                queue.append(nextlevel)
        return res
        
        