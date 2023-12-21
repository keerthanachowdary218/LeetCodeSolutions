class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ''
        max_length = 0
        for index in range(len(s)):
            last_index = len(s) - 1
            while s[index : last_index + 1] != s[index : last_index + 1][::-1]:
                last_index = last_index - 1
            if (last_index - index + 1) > max_length:
                max_length = (last_index - index + 1)
                result = s[index : last_index + 1]
        return result