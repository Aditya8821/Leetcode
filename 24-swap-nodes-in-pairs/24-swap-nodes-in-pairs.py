# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous=dummy=ListNode(0)
        dummy.next=head
        while head and head.next:
            temp=head.next
            head.next=temp.next
            temp.next=head
            previous.next=temp
            previous=temp.next
            head=head.next
        return dummy.next