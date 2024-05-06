class Solution:
    def firstUniqChar(self, s: str) -> int:
        Hashh = {}
        for i in s:
            if i in Hashh:
                Hashh[i] += 1
            else:
                Hashh[i]=1
        for i in range(len(s)):
            if Hashh[s[i]] == 1:
                return i
        return -1
        