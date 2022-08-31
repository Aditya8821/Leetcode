# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ind=1
        odd=startodd=ListNode(0)
        even=starteven=ListNode(0)
        while head:
            if ind%2!=0:
                odd.next=head
                odd=odd.next
            else:
                even.next=head
                even=even.next
            head=head.next
            ind+=1
        even.next=None
        odd.next=starteven.next
        return startodd.next