class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for num in nums:
            xor ^= num
        set_bit = xor & -xor
        a, b = 0, 0
        for num in nums:
            if num & set_bit:
                a ^= num
            else:
                b ^= num
        return [a, b]
        #https://leetcode.com/problems/single-number-iii/discuss/5233092/Proper-Interview-Solution-by-cs_iitian
        '''
        Example: nums = [1, 2, 1, 3, 2, 5]

Step 1: Compute XOR of all elements: 
1 ^ 2 ^ 1 ^ 3 ^ 2 ^ 5 = 3 ^ 5 = 6 (In binary: 0110)

Step 2: Find rightmost set bit of 6:
6 & -6 = 2 (In binary: 0010)

Step 3: Partition numbers based on the rightmost set bit:
- Group 1 (bit set at 2nd position): [2, 2, 3]
- Group 2 (bit not set at 2nd position): [1, 1, 5]

Step 4: XOR numbers within each group:
- Group 1: 2 ^ 2 ^ 3 = 3
- Group 2: 1 ^ 1 ^ 5 = 5

Result: [3, 5]
'''