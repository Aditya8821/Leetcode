"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return
        dummy=head
        while dummy:
            copy=Node(dummy.val)
            copy.next=dummy.next
            dummy.next=copy
            dummy=copy.next
        dummy=head
        dummy_cp=head.next
        while dummy.next.next:
            dummy_next=dummy.next.next
            dummy_cp.next=dummy_next.next
            if dummy.random:
                dummy_cp.random=dummy.random.next
            else:
                dummy_cp.random=None
            dummy=dummy_next
            dummy_cp=dummy_cp.next
        if dummy.random:
            dummy_cp.random=dummy.random.next
        else:
            dummy_cp.random=None
        return head.next