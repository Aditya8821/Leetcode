# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        d=collections.defaultdict(list)
        temp=[(root,0)]
        while temp:
            next=[]
            for value,pos in temp:
                d[pos].append(value.val)
                if value.left: next.append((value.left,pos-1))
                if value.right: next.append((value.right,pos+1))
                next.sort(key = lambda x: (x[1],x[0].val)) #the next will sort according to x[0].val in cases like example 2
            temp=next
        for k in sorted(d):
            res.append(d[k])
        return res
        
        
        
         
        