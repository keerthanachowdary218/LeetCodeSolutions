from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = Counter(nums)
        bucket = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            bucket[freq].append(num)
        res = []
        for i in range(len(nums), 0, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res
        