class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        candySet=set()
        for i in candyType:
            if i not in candySet:
                candySet.add(i)
        setlen=len(candySet)
        n=len(candyType)
        if setlen >= n // 2:
            return n // 2
        else:
            return setlen
