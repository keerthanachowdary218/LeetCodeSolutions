class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat)*len(mat[0])==c*r:
            arr=[]
            for i in range(len(mat)):
                for j in range(len(mat[0])):
                    arr.append(mat[i][j])
            newmat=[[0 for i in range(c)] for j in range(r)]
            ind=0
            for i in range(r):
                for j in range(c):
                    newmat[i][j]=arr[ind]
                    ind=ind+1
            return newmat
            
        else:
            return mat
        