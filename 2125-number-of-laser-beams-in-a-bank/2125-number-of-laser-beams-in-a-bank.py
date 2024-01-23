class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev=0
        result=0
        for i in bank:
            n=i.count('1')
            if n == 0:
                    continue
            else:
                result=result+prev*n
            prev=n
        return result