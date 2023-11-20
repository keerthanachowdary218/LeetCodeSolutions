# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        dA=headA
        i1=0
        while dA:
            dA=dA.next
            i1=i1+1
        dB=headB
        i2=0
        while dB:
            dB=dB.next
            i2=i2+1
        diff=i1-i2
        #print("diff",diff)
        if(diff>0):
            for i in range(0,diff):
                headA=headA.next
                i=i+1
        elif(diff<0):
            diff=diff*(-1)
            for i in range(0,diff):
                headB=headB.next
                i=i+1
        #print(headA.val,headB.val)
        while headA and headB and headA!=headB:
            headA=headA.next
            headB=headB.next
            #print(headA.val,headB.val)
        #print(headA.val,headB.val)
        if headA==headB and headA!=None:
            print("Intersected at", headA.val)
            return headA
        else:
            print("No intersection")
            return None
        