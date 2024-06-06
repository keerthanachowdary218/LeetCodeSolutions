class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==1:
            return True
        elif n<0:
            return False
        else:
            while n>1:
                n=n/2
                if n==1:
                    return True
            return False