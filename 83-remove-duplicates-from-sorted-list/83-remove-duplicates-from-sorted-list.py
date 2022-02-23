# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        curr=head
        s=set()
        while curr:
            if curr.val in s:
                prev.next=curr.next
                curr=curr.next
            else:
                s.add(curr.val)
                prev=curr
                curr=curr.next
        return head