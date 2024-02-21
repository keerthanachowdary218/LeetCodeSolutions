class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums)==1:
            if nums[0]==target:
                return 0
            else:
                return -1
        if len(nums)==2:
            if nums[0]==target:
                return 0
            elif nums[1]==target:
                return 1
            else:
                return -1
        mid=len(nums)//2
        l=0
        r=len(nums)-1
        if nums[l]<nums[mid]:
            if nums[l]<=target<nums[mid]:
                print("first half",nums[l:mid])
                k= self.search(nums[l:mid+1],target)
                if k==-1:
                    return -1
                else:
                    return k
            
            else:
                print("secnd half",nums[mid:],(mid-1) )
                k=self.search(nums[mid:],target)
                if k==-1:
                    return -1
                else:
                    return (mid) +k
        elif nums[l]>nums[mid]:
            if nums[mid]<target<=nums[r]:
                k=self.search(nums[mid:],target)
                if k==-1:
                    return -1
                else:
                    return (mid) +k
            else:
                print("first half",nums[l:mid])
                k= self.search(nums[l:mid+1],target)
                if k==-1:
                    return -1
                else:
                    return k
        return -1
            
        
        
        
        
        