# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        prev=head
        curr=prev.next
        while curr:
            if prev.val==curr.val  :
                if not prev.next or not curr:
                    prev.next=None
                    curr=None
                    continue
                prev.next=curr.next
                curr=curr.next
            else:
                prev=curr
                curr=curr.next
        return head
                
    
    
        
        