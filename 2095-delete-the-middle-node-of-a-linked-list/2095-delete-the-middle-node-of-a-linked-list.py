# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next==None:
            return None
        prev,slow,fast=head,head,head
        while fast and fast.next:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        temp=prev.next
        prev.next=prev.next.next
        del temp
        return head