class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row=len(matrix)
        col=len(matrix[0])
        look=-1
        for i in range(0,row):
            print(matrix[i][0])
            if(matrix[i][0]<=target):
                look=i
        print(look)
        if(look==-1):
            return False
        print(matrix[look][int(col/2)])
        if (target>=matrix[look][int(col/2)]):
            print("first half",int(col/2))
            for i in range(col-1,(int(col/2)-1),-1):
                if(matrix[look][i]==target):
                    return True    
        elif(matrix[look][int(col/2)]>=target):
            print("secnd half",int(col/2))
            for i in range(0,(int(col/2)+1)):
                if(matrix[look][i]==target):
                    return True
        return False
            
        
                
            
        