class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        '''
        i=0
        while k>0:
            #print(i)
            k=k-chalk[i]
            i=i+1
            if i>=len(chalk):
                i=i%len(chalk)
        if k==0:
            return i
        if k<0:
            return (i-1)%len(chalk)
        '''
        total_chalk = sum(chalk)
        k = k % total_chalk  # Reduce k to be within the range of one full cycle
        
        i = 0
        while k >= chalk[i]:
            k -= chalk[i]
            i += 1
        
        return i