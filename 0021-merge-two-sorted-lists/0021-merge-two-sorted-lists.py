# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p=ListNode()
        ans=p
        while(list1 and list2):
            if list1.val<list2.val:
                temp=list1.next      
                p.next=list1
                p=list1
                list1=temp
            else:
                temp=list2.next           
                p.next=list2
                p=list2
                list2=temp
        if list1 or list2:
            p.next = list1 if list1 else list2   
        return ans.next