class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        '''
        #O(n^2) time complexity
        c=0
        for i in range(0,len(nums)):
            for j in range(i,len(nums)):
                if j-i!=nums[j]-nums[i]:
                    c+=1
        return c
        '''
        diff_map = defaultdict(int)
        total_pairs = 0 
        good_pairs = 0 
        for i in range(len(nums)):
            diff = nums[i] - i
            good_pairs += diff_map[diff]  # Add the frequency of the current difference
            diff_map[diff] += 1  # Update the frequency map
            total_pairs += i  # Total pairs is the sum of the first (n-1) integers
        return total_pairs - good_pairs