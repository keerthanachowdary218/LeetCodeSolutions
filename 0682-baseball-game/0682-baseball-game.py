class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        score = []
        sum = 0
        n = -1
        for i in operations:
            if i.lstrip('-').isdigit() == True:
                score.append(int(i))
                n += 1
            elif i == "+":
                score.append(score[n-1]+score[n])
                n += 1
            elif i == "D":
                score.append(score[n]*2)
                n += 1
            elif i == "C":
                score.pop()
                n -= 1
            
        for i in range (0, n + 1):
            sum += score[i]
        return sum