class Solution(object):
    def lenLongestFibSubseq(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if len(arr) <= 2:
            return 0
        index_map = {num: i for i, num in enumerate(arr)}
        maxi = 0
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                prev, prevv = arr[j], arr[i]
                length = 2
                while prev + prevv in index_map:
                    length += 1
                    maxi = max(maxi, length)
                    prev, prevv = prev + prevv, prev
        return maxi if maxi > 2 else 0
        