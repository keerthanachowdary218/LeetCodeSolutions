# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head
        prev=head
        while prev.next:
            if prev.next.val==val:
                prev.next=prev.next.next
            else:
                prev=prev.next
        if head.val==val:
            head=head.next
        return head
                
                
                
        