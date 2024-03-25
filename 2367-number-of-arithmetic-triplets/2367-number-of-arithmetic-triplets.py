class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count=0
        def isInList(n):
            for i in nums:
                if i==n:
                    return True
            return False
        for i in nums:
            j=i+diff
            k=j+diff
            if isInList(j) and isInList(k):
                count=count+1
        return count
    