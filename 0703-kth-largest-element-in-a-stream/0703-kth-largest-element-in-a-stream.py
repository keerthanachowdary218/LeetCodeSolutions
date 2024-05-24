class KthLargest:
    '''
    def __init__(self, k: int, nums: List[int]):
        self.nums=nums
        self.k=k

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort()
        self.nums=self.nums[::-1]
        return self.nums[self.k-1]
     '''
    #below uses minheap
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = []
        for num in nums:
            heapq.heappush(self.minHeap, num)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)         # Only keeping k maximum elements

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)       # first add to min heap
        
        if len(self.minHeap) > self.k:          # if length greater pop minimum element as root is the min
            heapq.heappop(self.minHeap)
            
        return self.minHeap[0]
    

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)