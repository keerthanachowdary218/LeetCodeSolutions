class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original)!=m*n:
            return []
        arr=[[0 for i in range(n)] for j in range(m)]
        j=0
        for i in range(m):
            print(original[j:j+n])
            arr[i]=original[j:j+n]
            j+=n
        return (arr)