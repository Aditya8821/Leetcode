# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        curr=head
        d={}
        while curr:
            if curr.val in d:
                prev.next=curr.next
                curr=curr.next
            else:
                d[curr.val]=0
                prev=curr
                curr=curr.next
        return head