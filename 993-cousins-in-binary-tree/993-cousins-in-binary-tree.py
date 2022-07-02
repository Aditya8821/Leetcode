# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root: return []
        queue=[[root]]
        output=[]
        while queue:
            level=queue.pop(0)
            output.append([item.val for item in level])
            nextlevel=[]
            for item in level:
                if item.left:
                    nextlevel.append(item.left)
                if item.right:
                    nextlevel.append(item.right)
                if item.left and item.right and (item.left.val==x and item.right.val==y or item.left.val==y and item.right.val==x):
                    return False
            if nextlevel:
                queue.append(nextlevel)
        for i in output:
            if x in i and y in i:
                return True
        return False
                    
        