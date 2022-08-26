# Definition for singly-linked list.
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp1=temp2=Node(0)
        carry=0
        while l1 or l2 or carry:
            val1=val2=0
            if l1:
                val1=l1.val
                l1=l1.next
            if l2:
                val2=l2.val
                l2=l2.next
            total=val1+val2+carry
            val=total%10
            carry=total//10
            temp1.next=Node(val)
            temp1=temp1.next
        return temp2.next
    
    