# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcdd(x,y):
            if y==0:
                return abs(x)
            return gcdd(y, x%y)
        curr=head
        if not head or not head.next:
            return head
        while curr.next:
            gcdval=gcdd(curr.val,curr.next.val)
            newnode=ListNode(gcdval,curr.next)
            curr.next=newnode
            curr=curr.next.next
        return head
            
            