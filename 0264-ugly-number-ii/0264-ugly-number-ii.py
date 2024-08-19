class Solution:
    def nthUglyNumber(self, n: int) -> int:
        '''
        #time exceeded
        res=[1]
        num=2
        def isUgly(n):
            if n>0:
                for p in [2,3,5]:
                    while n%p==0:
                        n=n//p
            if n==1:
                return True
            else:
                False
        #print(isUgly(9))
        while len(res)<n:
            if isUgly(num):
                res.append(num)
            num+=1
        #print(res)
        return res[n-1]
        '''
        ugly = [1]
        
        # Initialize pointers for multiples of 2, 3, and 5
        i2 = i3 = i5 = 0
        
        # Continue generating ugly numbers until we reach the nth one
        while len(ugly) < n:
            # Calculate the next candidates for ugly numbers
            next_ugly_2 = ugly[i2] * 2
            next_ugly_3 = ugly[i3] * 3
            next_ugly_5 = ugly[i5] * 5
            
            # Choose the smallest candidate
            next_ugly = min(next_ugly_2, next_ugly_3, next_ugly_5)
            ugly.append(next_ugly)
            
            # Increment the corresponding pointer(s)
            if next_ugly == next_ugly_2:
                i2 += 1
            if next_ugly == next_ugly_3:
                i3 += 1
            if next_ugly == next_ugly_5:
                i5 += 1
        
        # Return the nth ugly number
        return ugly[n-1]
    