class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=""
        v=sorted(strs)
        first=v[0]
        last=v[-1]
        print(v)
        for i in range(min(len(first),len(last))):
            if(first[i]!=last[i]):
                return ans
            ans+=first[i]
        return ans 