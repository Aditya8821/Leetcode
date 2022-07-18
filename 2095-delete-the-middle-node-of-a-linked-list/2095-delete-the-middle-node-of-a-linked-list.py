# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #for removing that extra prev pointer from below 1st approach
        if head.next==None:
            return None
        slow,fast=head,head.next.next
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
        temp=slow.next
        slow.next=slow.next.next
        del temp
        return head
        
        
        
        
        # 1st approach
        # if head.next==None:
        #     return None
        # prev,slow,fast=head,head,head
        # while fast!=None and fast.next!=None:
        #     prev=slow
        #     slow=slow.next
        #     fast=fast.next.next
        # temp=prev.next
        # prev.next=prev.next.next
        # del temp
        # return head