from collections import deque
class MyStack:
    def __init__(self):
        self.queue = deque()
    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
		# push new element into queue's tail
        self.queue.append(x)
        # make new element on the head position by rotation
        ''' 
        for _ in range(len(self.queue)-1):
            self.queue.append( self.queue.popleft() )
        '''
    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
		# pop head element of queue
        return self.queue.pop()
    def top(self) -> int:
        """
        Get the top element.
        """
		# return head element of queue
        n=len(self.queue)-1
        return self.queue[n]
    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return (not self.queue)

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()