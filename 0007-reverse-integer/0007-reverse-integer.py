class Solution:
    def reverse(self, x: int) -> int:
        if -2**31 <= x and x < 0:
            x=x*(-1)
            x=str(x)
            x=x[::-1]
            x=int(x)
            x=x*(-1)
        elif x <= (2**31 - 1):
            x=str(x)
            x=x[::-1]
            x=int(x)
            print(x)
        #they asked to return 0 if after conversion the x is not in range of [-231, 231 - 1]
        if -2**31 <= x and x <= (2**31 - 1):
            return x
        else:
            return 0
            