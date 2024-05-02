class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        hashh={}
        for i in nums:
            if i<0:
                i=i*-1
                if i not in hashh:
                    hashh[i]=['n']
                else:
                    if 'n' not in hashh[i]:
                        hashh[i].append('n')
            elif i>0:
                if i not in hashh:
                    hashh[i]=['p']
                else:
                    if 'p' not in hashh[i]:
                        hashh[i].append('p')
        print(hashh)
        maxi=-1
        for i in hashh:
            if len(hashh[i])==2:
                maxi=max(maxi,i)
        return maxi