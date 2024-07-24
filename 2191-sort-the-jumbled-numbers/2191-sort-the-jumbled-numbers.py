class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def map_number(num):
            mapped_num = ''.join(str(mapping[int(digit)]) for digit in str(num))
            return int(mapped_num)
        mapped_pairs = [(num, map_number(num)) for num in nums]
        sorted_pairs = sorted(mapped_pairs, key=lambda x: x[1])
        
        result = [pair[0] for pair in sorted_pairs]
        return result
        
        