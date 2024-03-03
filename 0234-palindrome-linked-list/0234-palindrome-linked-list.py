# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        lisst=[]
        pointer=head
        while pointer:
            lisst.append(pointer.val)
            pointer=pointer.next  
        if lisst==lisst[::-1]:
            return True
        else:
            return False
            
            
        
        