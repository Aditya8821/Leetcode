# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def iterate(self,l,root):
        if not root: return 
        l.append(root.val)
        self.iterate(l,root.left)
        self.iterate(l,root.right)
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        l=[]
        self.iterate(l,root)
        if len(l)<2 or len(set(l))<2:
            return -1
        else:
            s=set(l)
            l2=list(s)
            l2.sort()
            return l2[1]
        
        
        