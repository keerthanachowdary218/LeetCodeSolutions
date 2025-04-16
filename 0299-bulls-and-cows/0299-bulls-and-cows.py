class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bulls=0
        cows=0
        counts=Counter(secret)
        for i in range(len(secret)):
            if secret[i]==guess[i]:
                bulls+=1
                counts[secret[i]]-=1
        #print(counts)
        for i in range(len(secret)):
            if secret[i]!=guess[i]:
                if guess[i] in counts and counts[guess[i]]>0:
                    cows+=1
                    counts[guess[i]]-=1
        #res=str(bulls)+'A'+str(cows)+'B'
        return str(bulls)+'A'+str(cows)+'B'


        