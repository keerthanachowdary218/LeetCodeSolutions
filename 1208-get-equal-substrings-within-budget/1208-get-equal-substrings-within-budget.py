class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        '''
        max_length = 0
        for i in range(len(s)):
            current_cost = 0
            for j in range(i, len(s)):
                current_cost += abs(ord(s[j]) - ord(t[j]))
                if current_cost > maxCost:
                    break  # Stop expanding this substring since it exceeds maxCost
                max_length = max(max_length, j - i + 1)
        return max_length
        '''
        #below used sliding window so it wont exceed in time limit
        n = len(s)
        start = 0
        current_cost = 0
        max_length = 0
        for end in range(n):
            current_cost += abs(ord(s[end]) - ord(t[end]))
            while current_cost > maxCost:
                current_cost -= abs(ord(s[start]) - ord(t[start]))
                start += 1
            max_length = max(max_length, end - start + 1)
        return max_length

    
    
        