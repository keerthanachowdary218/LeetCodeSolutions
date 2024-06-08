class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        '''
        #below is wrong because keys should be unique - names are not unique
        dictt={}
        for i,name in enumerate(names):
            dictt[name]=heights[i]
        dictt=sorted(dictt.items(),key=lambda item: item[1])
        res=[]
        for name,height in dictt:
            res.append(name)
        return (res[::-1])
        '''
        dictt={}
        for i,height in enumerate(heights):
            dictt[height]=names[i]
        dictt=sorted(dictt.items(),key=lambda item: item[0])
        #print(dictt)
        res=[]
        for height,name in dictt:
            res.append(name)
        res=res[::-1]
        return res
        
        