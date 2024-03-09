class Solution:
    def addDigits(self, num: int) -> int:
        if len(str(num))==1:
            return num
        else:
            num=sum(int(i) for i in str(num))
            k=self.addDigits(num)
            return k