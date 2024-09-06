# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        if not head:
            return None
        num_hash = set(nums)
        dummy = ListNode(0)
        dummy.next = head
        prev, node = dummy, head
        while node:
            if node.val in num_hash:
                prev.next = node.next
            else:
                prev = node
            node = node.next
        return dummy.next
        '''
        if not head:
            return None
        num_hash = set(nums)
        node=head.next
        prev=head
        while node:
            if node.val in num_hash:
                prev.next=node.next
            else:
                prev=node
            node=node.next
        if head.val in num_hash:
            head=head.next
        return head
        
        