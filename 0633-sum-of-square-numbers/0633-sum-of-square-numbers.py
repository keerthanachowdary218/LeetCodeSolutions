class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        '''
        if c%2!=0:
            c=c-1
        for i in range(1,c+1):
            if i==(c/i):
                return True
        return False
        '''
        for a in range(int(sqrt(c)) + 1):  # Iterate through all possible values of `a`
                b = sqrt(c - a * a)  # Compute `b` as the square root of `c - a^2`
                if b == int(b):  # Check if `b` is an integer
                    return True  # If `b` is an integer, return true
        return False  # If no such pair `(a, b)` is found, return false
