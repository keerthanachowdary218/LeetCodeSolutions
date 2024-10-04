class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill=sorted(skill)
        print(skill)
        reqskill=skill[0]+skill[-1]
        i,j=0,len(skill)-1
        ans=0
        while i<j:
            if skill[i]+skill[j]==reqskill:
                ans+=skill[i]*skill[j]
            else:
                return -1
            i+=1
            j-=1
        return ans