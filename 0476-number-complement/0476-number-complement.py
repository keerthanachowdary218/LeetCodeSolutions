class Solution:
    def findComplement(self, num: int) -> int:
        binary = bin(num)[2:]
        flipped_binary = ''.join(['0' if bit == '1' else '1' for bit in binary])
        return int(flipped_binary, 2)
        
        