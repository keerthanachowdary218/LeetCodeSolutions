class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #print(matrix)
        n=len(matrix)
        #print(n)
        m=len(matrix[0])
        #print(m)
        #donot use check=[0*m]*n
        check = [[0 for i in range(0,m)] for j in range(0,n)]
        #print(check)
        for i in range(0,n):
            for j in range(0,m):
                if(matrix[i][j]==0):
                    #print(i,j)
                    check[i][j]=1
        #print(check)
        for i in range(0,n):
            for j in range(0,m):
                if(check[i][j]==1):
                    for k in range(0,m): 
                        matrix[i][k]=0
                    for k in range(0,n):
                        matrix[k][j]=0
        print(matrix)
        return matrix
        
        
