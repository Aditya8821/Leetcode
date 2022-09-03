# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1,s2=[],[]
        while l1 or l2:
            if l1:
                s1.append(l1.val)
                l1=l1.next
            if l2:
                s2.append(l2.val)
                l2=l2.next
        nxt=None
        carry=0
        while s1 or s2 or carry:
            if s1:
                carry+=s1.pop()
            if s2:
                carry+=s2.pop()
            val=carry%10
            carry=carry//10
            curr=ListNode(val)
            curr.next=nxt
            nxt=curr
        return curr
        