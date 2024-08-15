class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        prevsum=0
        arrays=[0,0,0]
        for bill in bills:
            if bill==5:
                arrays[0]+=1
                continue
            elif bill==10:
                arrays[1]+=1
                if arrays[0]>0:
                    arrays[0]-=1
                    continue
                else:
                    return False
            elif bill==20:
                arrays[2]+=1
                if arrays[0]>0 and arrays[1]>0 :
                    arrays[0]-=1
                    arrays[1]-=1
                elif arrays[0]>=3:
                    arrays[0]-=3
                else:
                    return False
        return True
            
        
        