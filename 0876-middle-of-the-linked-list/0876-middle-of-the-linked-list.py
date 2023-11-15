# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #naive solution
        '''n=0
        listt=head
        while(head):
            n=n+1
            head=head.next
        print(n)
        if(n>0):
            for i in range(0,int(n/2)):
                i=i+1
                listt=listt.next
        return listt'''
        #optimized
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
                
                
        