from collections import Counter
class Solution:
    def maxDifference(self, s: str) -> int:
        count=Counter(s)
        maxodd=0
        mineven = float('inf')
        for i in count:
            if count[i] % 2 != 0:
                maxodd = max(maxodd, count[i])
            else:
                mineven = min(mineven, count[i])
        return maxodd - mineven