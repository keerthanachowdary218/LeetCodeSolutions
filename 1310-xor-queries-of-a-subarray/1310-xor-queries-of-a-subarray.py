class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        prefix = [0] * n
        ans = []
        prefix[0] = arr[0]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] ^ arr[i]
        

        #a^0 is a and a^a is 0
        for left, right in queries:
            if left == 0:
                ans.append(prefix[right])
            else:
                ans.append(prefix[right] ^ prefix[left - 1])

        return ans
            
        '''   
        res=[]
        for i,j in queries:
            curr=arr[i]
            for k in range(i+1,j+1):
                curr=curr ^ arr[k]
            res.append(curr)
        return res
        '''