# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        listt=head
        arr=0
        count=0
        while listt:
            arr=arr*10+listt.val
            listt=listt.next
            count+=1
        arr=arr*2
        arr=str(arr)
        listt=head
        count=0
        while listt:
            listt.val=arr[count]
            count+=1
            prev=listt
            listt=listt.next
        print(count)
        if count!=len(arr):
            newnode=ListNode(arr[count])
            prev.next=newnode
        return head
        #limit exceeds - the str part.
        '''
        values = []
        val = 0

        # Traverse the linked list and push its values onto the list
        while head is not None:
            values.append(head.val)
            head = head.next

        new_tail = None

        # Iterate over the list of values and the carryover
        while values or val != 0:
            # Create a new ListNode with value 0 and the previous tail as its next node
            new_tail = ListNode(0, new_tail)

            # Calculate the new value for the current node
            # by doubling the last digit, adding carry, and getting the remainder
            if values:
                val += values.pop() * 2
            new_tail.val = val % 10
            val //= 10

        # Return the tail of the new linked list
        return new_tail
        
            
        