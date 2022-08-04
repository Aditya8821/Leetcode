# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue=[[root]]
        ans=[]
        while queue:
            level=queue.pop()
            x=level[-1]
            ans.append(x.val)
            nextlevel=[]
            for item in level:
                if item.left:
                    nextlevel.append(item.left)
                if item.right:
                    nextlevel.append(item.right)
            if nextlevel:
                queue.append(nextlevel)
        return ans