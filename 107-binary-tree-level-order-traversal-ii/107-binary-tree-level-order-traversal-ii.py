# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
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
            if nextlevel:
                queue.append(nextlevel)
        return reversed(output)