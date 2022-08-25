"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return None
        q=[root]
        while q:
            nextnode=None
            for _ in range(len(q)):
                curr=q.pop(0)
                curr.next,nextnode=nextnode,curr
                if curr.right:
                    q.extend([curr.right,curr.left])
        return root
        