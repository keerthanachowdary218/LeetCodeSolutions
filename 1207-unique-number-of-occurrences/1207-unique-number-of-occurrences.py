class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        result={}
        for i in range(0,len(arr)):
            if arr[i] in result.keys():
                result[arr[i]]+=1
            else:
                result[arr[i]]=1
        print(result.values())
        print(set(result.values()))
        if len(result.values())==len(set(result.values())):
            return True
        else:
            return False
            
            
        