# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp1=temp2=ListNode(0)
        while l1 and l2:
            if l1.val<l2.val:
                temp1.next=ListNode(l1.val)
                l1=l1.next
            else:
                temp1.next=ListNode(l2.val)
                l2=l2.next
            temp1=temp1.next
        temp1.next=l1 or l2
        return temp2.next
