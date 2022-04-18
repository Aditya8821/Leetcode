# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        answer=[]
        def solve(root):
            if not root:
                return
            solve(root.left)
            answer.append(root.val)
            solve(root.right)
        solve(root)
        heapify(answer)
        
        for i in range(1,k+1):
            if i is k:
                value = heappop(answer)
                break
            heappop(answer)
        return value