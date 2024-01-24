class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        if len(x)%2==0 and x[0:(len(x)//2)]==(x[len(x)//2:][::-1]):
            return True
        if len(x)%2!=0 and x[0:(len(x)//2)+1]==(x[len(x)//2:][::-1]):
            return True
        else:
            return False