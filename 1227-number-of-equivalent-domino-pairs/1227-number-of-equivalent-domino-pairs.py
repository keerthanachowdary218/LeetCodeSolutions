class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        '''
        res=0
        for i in range(len(dominoes)):
            for j in range(i+1,len(dominoes)):
                if (dominoes[i][0]==dominoes[j][0] and dominoes[i][1]==dominoes[j][1]) or (dominoes[i][1]==dominoes[j][0] and dominoes[i][0]==dominoes[j][1]):
                    res+=1
        return res
        '''
        hashh={}
        for i in range(len(dominoes)):
            key=(min(dominoes[i][0],dominoes[i][1]), max(dominoes[i][0],dominoes[i][1]))
            if key in hashh:
                hashh[key]+=1
            else:
                hashh[key]=1
        summ=0
        for i in hashh:
            if hashh[i] > 1:
                summ += hashh[i] * (hashh[i] - 1) // 2
        return (summ)



        