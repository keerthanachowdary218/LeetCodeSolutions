class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        maxi=0
        while l<r:
            if height[l]<=height[r]:
                currvol=(height[l])*(r-l)
                l=l+1
            else:
                currvol=(height[r])*(r-l)
                r=r-1
            print(currvol)
            maxi=max(maxi,currvol)
        return (maxi)
            
        