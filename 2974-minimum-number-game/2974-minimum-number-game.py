class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        arr=[]
        alice=[]
        bob=[]
        i=0
        for i in range(0,len(nums)):
            if i%2==0:
                alice.append(nums[i])
            else:
                bob.append(nums[i])
        for i in range(0,len(nums)):
            if i%2==0:
                arr.append(bob[i//2])
            else:
                arr.append(alice[i//2])
        return arr
        