class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        #brute force- not inplace
        #lexicographyically is nothing but dictonary order
        n=len(nums)
        index=-1
        ans=[]
        for i in range(n-1,-1,-1):
            if nums[i-1]<nums[i]:
                index=i-1
                break;
        #print(index)
        if(index==-1):
            for i in range(n-1,-1,-1):
                ans.append(nums[i])
            print(ans)
            return ans
        else:
            for i in range(n-1,index,-1):
                if nums[i]>nums[index]:
                    #basically swapping- you can use swap function too.
                    temp=nums[index]
                    nums[index]=nums[i]
                    nums[i]=temp
                    break;
            for i in range(0,index+1):
                ans.append(nums[i])
            for i in range(n-1,index,-1):
                ans.append(nums[i])
            return ans
        print("ok")
        '''
        n=len(nums)
        index=-1
        ans=[]
        for i in range(n-1,-1,-1):
            if nums[i-1]<nums[i]:
                index=i-1
                break;
        #print(index)
        if(index==-1):
            nums.reverse()
        else:
            print(nums)
            print(index)
            for i in range(n-1,index,-1):
                if nums[i]>nums[index]:
                    #basically swapping- you can use swap function too.
                    temp=nums[index]
                    nums[index]=nums[i]
                    nums[i]=temp
                    break;
            #reversing the array from index+1 to end of the array
            nums[index + 1:] = nums[index + 1:][::-1]

        
                
            