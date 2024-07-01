class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones)==1:
            return stones[0]
        stones= [stone*-1 for stone in stones]
        heapq.heapify(stones)
        while len(stones)>1:
            x=heapq.heappop(stones)
            y=heapq.heappop(stones)
            if x*(-1)!=y*(-1):
                heapq.heappush(stones,abs(x-y)*(-1))
        if len(stones)==1:
            return stones[0]*(-1)
        if len(stones)==0:
            return 0
        
        