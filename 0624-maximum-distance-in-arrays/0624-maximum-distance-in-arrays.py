class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        
        min_val = arrays[0][0]
        max_val = arrays[0][-1]
        max_dist = 0
        
        for i in range(1, len(arrays)):
            # Calculate the distance with current array's min and previous max
            max_dist = max(max_dist, abs(arrays[i][-1] - min_val))
            # Calculate the distance with current array's max and previous min
            max_dist = max(max_dist, abs(max_val - arrays[i][0]))
            
            # Update the min and max values
            min_val = min(min_val, arrays[i][0])
            max_val = max(max_val, arrays[i][-1])
        
        return max_dist
        