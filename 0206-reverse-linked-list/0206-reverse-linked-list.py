# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            print("head",head)
            return head
        dummy_node=None
        current_node=head
        # Head of the initial list will become the new tail
        while current_node:
            next_node = current_node.next
            current_node.next = dummy_node
            dummy_node = current_node
            current_node = next_node
        print(dummy_node)
        return dummy_node
    