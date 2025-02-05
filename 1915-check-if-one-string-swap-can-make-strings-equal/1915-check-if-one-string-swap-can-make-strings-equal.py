class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1)!=len(s2):
            return False
        if Counter(s1)!=Counter(s2):
            return False
        count=0
        for i in range(0,len(s1)):
            if s1[i]!=s2[i]:
                count+=1
        if count==0 or count==2:
            return True
        else:
            return False
        