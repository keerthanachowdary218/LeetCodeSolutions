# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        # Create a hash set from nums for O(1) lookups
        num_hash = set(nums)

        # Use a dummy node to simplify edge cases
        dummy = ListNode(0)
        dummy.next = head
        prev, node = dummy, head

        while node:
            if node.val in num_hash:
                # Remove the node if its value is in num_hash
                prev.next = node.next
            else:
                # Move the prev pointer only when the node is not removed
                prev = node
            node = node.next

        # Return the updated list starting from dummy.next
        return dummy.next
        '''
        if not head:
            return None
        node=head.next
        prev=head
        while node:
            if node.val in set(nums):
                prev.next=node.next
            else:
                prev=node
            node=node.next
        if head.val in set(nums):
            head=head.next
        return head
        '''
        