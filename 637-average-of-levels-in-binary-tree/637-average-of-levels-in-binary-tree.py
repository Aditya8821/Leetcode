# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root: return []
        queue=[[root]]
        output=[]
        while queue:
            level=queue.pop(0)
            s=0
            for item in level:
                s+=item.val
            x=s/len(level)
            output.append(x)
            nextlevel=[]
            for item in level:
                if item.left:
                    nextlevel.append(item.left)
                if item.right:
                    nextlevel.append(item.right)
            if nextlevel:
                queue.append(nextlevel)
        return output
            