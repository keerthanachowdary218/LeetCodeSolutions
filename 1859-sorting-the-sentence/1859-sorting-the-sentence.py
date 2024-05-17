class Solution:
    def sortSentence(self, s: str) -> str:
        splits=s.split()
        mapp={}
        for i in splits:
            mapp[i[-1]]=i[:-1]
        mapp = dict(sorted(mapp.items()))
        s=''
        count=0
        for i in mapp:
            if count==0:
                s+=mapp[i]
            else:
                 s+=' '+mapp[i]
            count+=1
        return s