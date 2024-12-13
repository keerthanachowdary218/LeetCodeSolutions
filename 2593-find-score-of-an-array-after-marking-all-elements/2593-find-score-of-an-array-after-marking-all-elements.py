class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        score = 0
        pq = [(nums[i], i) for i in range(n)]
        #print(pq)
        heapq.heapify(pq)
        visited = [False] * n
        while pq:
            val, index = heapq.heappop(pq)
            if visited[index]:
                continue
            if index - 1 >= 0:
                visited[index - 1] = True
            if index + 1 < n:
                visited[index + 1] = True
            score += val
        return score
        