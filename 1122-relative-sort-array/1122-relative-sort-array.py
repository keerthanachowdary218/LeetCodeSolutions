class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        mapp={}
        #creating a mapp with elemnts in order of arr2
        for i in arr2:
            mapp[i]=0
        rest=[]
        #counting elements in arr2 in arr1
        for i in arr1:
            if i in mapp:
                mapp[i]+=1
            else:
                rest.append(i)
        res=[]
        #appending in result array and also sorting the rest of the elements in array
        for i in mapp:
            for j in range(0,mapp[i]):
                res.append(i)
        res.extend(sorted(rest))
        return res