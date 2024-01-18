class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        result=[]
        for num in nums:
            if len(result)==0:
                result.append([num])
            else:
                flag = False
                for row in range(len(result)):
                    if num not in result[row]:
                        result[row].append(num)
                        flag = True
                        break
                if not flag:
                    result.append([num])
        return result
                
            
        