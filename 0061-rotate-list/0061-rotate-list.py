# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        listt=[]
        finalListNode=finalhead=head
        while finalhead:
                listt.append(finalhead.val)
                finalhead=finalhead.next
        length=len(listt) 
        if finalListNode:
            if k == length:
                return head
            k =  k % length
            if k == 0:
                return head
            for i in range(0,k):
                num=listt.pop()
                listt.insert(0,num)
                print(listt)
                i=i+1
            for i in range(0,len(listt)):
                head.val=listt[i]
                head=head.next
                i=i+1
        return finalListNode
        