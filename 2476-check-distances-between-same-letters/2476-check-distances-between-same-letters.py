class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        firstIndex = [-1] * 26 
        for i, char in enumerate(s):
            index = ord(char) - ord('a')
            if firstIndex[index] == -1:
                firstIndex[index] = i
            else:
                if i - firstIndex[index] - 1 != distance[index]:
                    return False
        return True

        