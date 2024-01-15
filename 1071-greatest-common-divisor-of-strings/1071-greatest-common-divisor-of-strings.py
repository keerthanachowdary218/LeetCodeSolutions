class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        '''
        if str1 + str2 != str2 + str1:
            return ""
        if len(str1) == len(str2):
            return str1
        if len(str1) > len(str2):
            print(str1[len(str2):])
            return self.gcdOfStrings(str1[len(str2):], str2)
        return self.gcdOfStrings(str1, str2[len(str1):])
        '''
        if str1 + str2 == str2 + str1:
                x = gcd(len(str1),len(str2))
                return str1[:x]
        else:
                return ""