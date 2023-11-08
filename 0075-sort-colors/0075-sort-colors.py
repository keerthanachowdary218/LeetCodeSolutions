class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        #brute force--but wouldnt be inplace algorithm
        zeroes=[]
        ones=[]
        twos=[]
        for i in nums:
            if i==0:
                zeroes.append(i)
            if i==1:
                ones.append(i)
            if i==2:
                twos.append(i)
        ans=[]
        ans=zeroes+ones+twos
        
        #print(ans)
        '''
        # optimal ->in place algorithm
        z=0
        h=len(nums)-1
        i=0
        while(i<=h):
            if nums[i]==0:
                nums[z],nums[i]=nums[i],nums[z]
                z=z+1
                i=i+1
                #print("0",nums)
            elif nums[i]==1:
                i=i+1
            elif nums[i]==2:  
                nums[i],nums[h]=nums[h],nums[i]
                h=h-1
         
                #print("2",nums)
        #return ans
    
    
    