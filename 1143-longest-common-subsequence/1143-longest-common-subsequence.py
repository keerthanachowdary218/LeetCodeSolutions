'''
class Solution:
    def f(self,str1,str2,dp):
        if not str1 or not str2:
            return 0
        if dp[len(str1)][len(str2)] != -1:
            return dp[len(str1)][len(str2)]
        if str1[0] == str2[0]:
            dp[len(str1)][len(str2)] = 1 + self.f(str1[1:], str2[1:], dp)
            return dp[len(str1)][len(str2)]
        else:
            dp[len(str1)][len(str2)] = max(self.f(str1[1:], str2, dp), self.f(str1, str2[1:], dp))
            return dp[len(str1)][len(str2)]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[-1 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]
        return self.f(text1, text2, dp)
    '''
class Solution:
    def f(self,str1,str2,dp):
        if not str1 or not str2:
            return 0
        if dp[len(str1)][len(str2)]!=-1 :
            return dp[len(str1)][len(str2)]
        if str1[0]==str2[0]:
            dp[len(str1)][len(str2)]=1+(self.f(str1[1:],str2[1:],dp))
            return dp[len(str1)][len(str2)]
        else:
            dp[len(str1)][len(str2)]=max(self.f(str1[1:],str2,dp),self.f(str1,str2[1:],dp))
            return dp[len(str1)][len(str2)]
        
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp=[[(-1) for x in range(len(text2)+1)] for x in range(len(text1)+1)]
        return (self.f(text1,text2,dp))