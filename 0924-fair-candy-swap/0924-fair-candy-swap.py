class Solution(object):
    def fairCandySwap(self, aliceSizes, bobSizes):
        """
        :type aliceSizes: List[int]
        :type bobSizes: List[int]
        :rtype: List[int]
        """
        diff=(sum(aliceSizes)-sum(bobSizes))//2;
        A=set(aliceSizes)
        for i in set(bobSizes):
            if i+diff in A:
                return [diff+i,i]
        