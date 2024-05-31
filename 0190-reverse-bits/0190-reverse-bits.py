class Solution:
    def reverseBits(self, n: int) -> int:
        n=bin(n)[2:].zfill(32) #converting to binary and padding with zeroes.
        return int(n[::-1],2)
        
        