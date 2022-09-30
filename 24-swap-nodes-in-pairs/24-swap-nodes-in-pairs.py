# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        prev=dum=ListNode
        while head and head.next:
            temp=head.next
            head.next=head.next.next
            prev.next=temp
            temp.next=head
            prev=head
            head=head.next
        return dum.next
            
        