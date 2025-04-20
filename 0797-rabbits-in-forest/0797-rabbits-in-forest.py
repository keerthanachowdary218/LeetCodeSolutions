from collections import Counter
class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        count = Counter(answers)
        res = 0
        for a, freq in count.items():
            #print(a,freq)
            group_size = a + 1
            groups = (freq + a) // group_size 
            res += groups * group_size
        return res
        