class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts=[-x for x in gifts]
        heapify(gifts)
        maxi, i= float(inf), 0
        while i<k and maxi>1:
            maxi=-heappop(gifts)
            heappush(gifts, -isqrt(maxi))
            i+=1
        return -sum(gifts)
        