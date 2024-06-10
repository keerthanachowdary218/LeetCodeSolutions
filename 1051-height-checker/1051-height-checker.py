class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected=sorted(heights)
        #print(expected)
        count=0
        for i,val in enumerate(expected):
            if val!=heights[i]:
                count+=1
        return count
            