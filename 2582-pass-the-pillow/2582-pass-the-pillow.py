class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        current_holder = 1
        direction = 1
        for _ in range(time):
            current_holder += direction
            if current_holder == n:
                direction = -1
            elif current_holder == 1:
                direction = 1
        return current_holder
        
            