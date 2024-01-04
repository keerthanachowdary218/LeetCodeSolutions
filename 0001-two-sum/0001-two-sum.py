class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        #bruteforce solution
        result=[]
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target and i!=j:
                    result.append(i)
                    result.append(j)
                    return result
        return result
        '''
        numMap = {}
        n = len(nums)
        # Build the hash table
        for i in range(n):
            numMap[nums[i]] = i
        # Find the complement
        print(numMap)
        for i in range(n):
            complement = target - nums[i]
            if complement in numMap and numMap[complement] != i:
                return [i, numMap[complement]]
        return []  # No solution found
        
    
        