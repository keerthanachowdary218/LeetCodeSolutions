class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n==1:
            return '1'
        prev=self.countAndSay(n-1)
        count = 1
        res=''
        for i in range(1, len(prev)):
            if prev[i] == prev[i - 1]:
                count += 1
            else:
                res += str(count) + prev[i - 1]
                count = 1
        res += str(count) + prev[-1]
        '''
        #doesnt take sequentially , 21-->gives 1112 not 1211, so we use above method
        count=Counter(prev)
        for i in count:
            res+=str(count[i])+''+i
        '''
        return res