class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        result = x ^ y
        #python automatically converts int to binary when performing xor operation
        return bin(result).count('1')