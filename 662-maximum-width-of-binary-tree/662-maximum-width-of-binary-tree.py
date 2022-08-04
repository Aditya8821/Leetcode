# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue=[(root,0)]
        maxdepth=0
        while queue:
            n=len(queue)
            for i in range(n):
                node,curr=queue.pop(0)
                if i==0:
                    start=curr
                if i==n-1:
                    end=curr
                if node.left:
                    queue.append((node.left,2*curr+1))
                if node.right:
                    queue.append((node.right,2*curr+2))
            maxdepth=max(maxdepth,end-start+1)
        return maxdepth
        
        
        
        # di = defaultdict(list)
        # def dfs(node, level, column):
        #     if node:
        #         di[level].append(column)
        #         dfs(node.left, level+1, column*2)
        #         dfs(node.right, level+1, column*2+1)
        # dfs(root, 0 , 0)
        # return max([max(di[level]) - min(di[level]) +1 for level in di])