class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count0=0
        count1=0
        for i in students:
            if i ==0:
                count0+=1
            else:
                count1+=1
        index=0
        while index<len(sandwiches):
            if sandwiches[index]==0 and count0>0:
                count0-=1
                index+=1
            elif sandwiches[index]==1 and count1>0:
                count1-=1
                index+=1
            else:
                break
        return count0+count1