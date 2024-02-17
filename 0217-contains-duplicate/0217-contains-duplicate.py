class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        countMap=set()
        for i in nums:
            if i not in countMap:
                countMap.add(i)
                print(i)
            else:
                return True
        return False
        