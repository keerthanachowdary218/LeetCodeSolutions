class Solution:
    def frequencySort(self, s: str) -> str:
        dicts={}
        for schar in s:
            if schar in dicts.keys():
                dicts[schar]+=1
            else:
                dicts[schar]=1
        sorted_dicts=sorted(dicts.items(),key=lambda x:x[1],reverse=True)
        res=""
        for i in sorted_dicts: 
            for count in range(0,i[1]):
                res+=i[0]
        return res
                
        