class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        res=0
        for i,seat in enumerate(seats):
            res+=abs(seat-students[i])
        return res