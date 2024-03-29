# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,start,end):
        if start>end:
            return [None]
        res=[]
        for i in range(start,end+1):
            left=self.helper(start,i-1)
            right=self.helper(i+1,end)
            for l in left:
                for r in right:
                    root=TreeNode(i)
                    root.left=l
                    root.right=r
                    res.append(root)
        return res
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n==0: return []
        return self.helper(1,n)