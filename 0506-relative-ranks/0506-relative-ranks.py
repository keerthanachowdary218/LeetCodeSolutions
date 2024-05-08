class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sortedscore=sorted(score)[::-1]
        count=3
        print(score,sortedscore)
        for i in range(0,len(score)):
            if score[i]==sortedscore[0]:
                score[i]='Gold Medal'
            elif score[i]==sortedscore[1]:
                score[i]='Silver Medal'
            elif score[i]==sortedscore[2]:
                score[i]='Bronze Medal'
            else:
                index = sortedscore.index(score[i])
                score[i]=str(index+1)
        return score
        
        
        