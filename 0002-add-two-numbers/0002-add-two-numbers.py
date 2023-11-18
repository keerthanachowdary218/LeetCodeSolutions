# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        len1=0
        head=l1
        while head:
            len1+=1
            head=head.next
        #print(len1)
        len2=0
        head=l2
        while head:
            len2+=1
            head=head.next
        #print(len2)
        head=l1
        num1=0
        for i in range(0,len1):
            dig1=head.val
            head=head.next
            num1=num1+dig1*(pow(10,i))
        #print(num1)
        head=l2
        num2=0
        for i in range(0,len2):
            dig2=head.val
            head=head.next
            num2=num2+dig2*(pow(10,i))
        #print(num2)
        sum=num1+num2
        print("sum",sum)
        i=0
        if(sum>0):
            while (sum/pow(10,i))>=1:
                i=i+1
        elif(sum==0):
            i=1
        print("i",i)
        ans=head=l3=ListNode()
        #digits = [int(x) for x in str(sum)]
        for k in range(0,i):
            dig=sum%10
            sum=sum//10
            #print(dig)
            head = ListNode(dig)
            l3.next = head
            l3 = l3.next
        l3=None
        return ans.next
            
        
        