class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        mat=[[0 for _  in range(n)] for _ in range(m)]
        for i in range(len(indices)):
            a=indices[i][0]
            b=indices[i][1]
            for j in range(n):
                mat[a][j]+=1
            for k in range(m):
                mat[k][b]+=1
        c=0        
        for i in range(m):
            for j in range(n):
                if mat[i][j]%2:
                    c+=1
        return c  
            