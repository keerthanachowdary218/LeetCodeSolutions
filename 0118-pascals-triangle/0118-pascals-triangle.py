class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        '''
        output=[]
        k=[]
        for i in range(0,numRows):
            row = [1] * (i+1)
            #print(row)
            output.append(row)
            print(output)'''
        row=[1]
        output = [row]
        #print("output",output)
        for _ in range(1, numRows):
            '''add 0 infront and the end..and do pairwise summation using map and make it to list at the end to append to output'''
            row = list(map(sum,pairwise([0]+row+[0])))
            output.append(row)
            #print(output)
        return output
         
         