# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        totallen=0
        ans=new=head
        while head:
            totallen+=1
            head=head.next
        print(totallen)
        k=totallen-n
        print(k)
        if(k>0):
            for i in range(0,k-1):
                new=new.next
                i=i+1
            if(new.next!=None):
                if(new.next.next!=None):
                    new.next=new.next.next
                else:
                    new.next=None
            else:
                ans.next=None
            return ans
        elif(k==0):
            return ans.next
        else:
            return -1
        