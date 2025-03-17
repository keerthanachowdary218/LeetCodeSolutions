class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        counts = Counter(nums)
        for i in counts:
            if counts[i]%2!=0:
                return False
        return True

        