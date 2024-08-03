class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        arrFreq = {}
        for num in arr:
            if num not in arrFreq:
                arrFreq[num] = 1
            else:
                arrFreq[num] += 1
        targetFreq = {}
        for num in target:
            if num not in targetFreq:
                targetFreq[num] = 1
            else:
                targetFreq[num] += 1
        if len(arrFreq) != len(targetFreq):
            return False

        for key in arrFreq:
            if arrFreq[key] != targetFreq.get(key, 0):
                return False
            
        return True