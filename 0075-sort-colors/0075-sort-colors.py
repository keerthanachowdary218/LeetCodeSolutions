class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        '''
        k=0
        for num in nums:
            if num==0:
                k+=1
        i,j=0,len(nums)-1
        while i<j:
            if nums[i]==0:
                i+=1
            elif nums[i]==2:
                nums[i],nums[j]=nums[j],nums[i]
                j-=1
            else:
                nums[i],nums[k]=nums[k],nums[i]
                k+=1
                i+=1
            print(nums)
        return nums
        '''
        red, white, blue = 0, 0, len(nums)-1
    
        while white <= blue:
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1
        return nums

            