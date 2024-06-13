class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        #sorting both seats and students and then finding the abs difference between them
        seats.sort()
        students.sort()
        res=0
        for i,seat in enumerate(seats):
            res+=abs(seat-students[i])
        return res