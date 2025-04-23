class Solution(object):
    def countLargestGroup(self, n):
        """
        :type n: int
        :rtype: int
        """
        hashh=defaultdict(int)
        for i in range(1,n+1):
            summ=0
            for dig in str(i):
                summ+=int(dig)
            hashh[summ]+=1
        maximum=max(hashh.values())
        res=0
        for i in hashh:
            if hashh[i]==maximum:
                res+=1
        return res
        print(hashh)
        #return n%9
