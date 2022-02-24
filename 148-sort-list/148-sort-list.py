# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return head
        def merge(a,b):   
            if not a:
                return b
            if not b :
                return a
            if a.val<b.val:
                a.next=merge(a.next,b)
                return a
            else:
                b.next=merge(a,b.next)
                return b
        
        
        #here we are breaking the list in 2 parts
        prev,slow,fast=None,head,head
        while fast and fast.next:
            prev,slow,fast=slow,slow.next,fast.next.next
        prev.next=None
        
        #here we are sorting those 2 lists separately and then merging them 
        first_half=self.sortList(head)
        second_half=self.sortList(slow)
        temp=merge(first_half,second_half)
        return temp
        