class Solution:
    def dayOfYear(self, date: str) -> int:
        words=date.split('-')
        y=int(words[0])
        m=int(words[1])
        d=int(words[2])
        #print(y,m,d)
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if (y % 400) == 0 or ((y % 4 == 0) and (y % 100 != 0)): days[1] = 29
        #print(days[:m-1])
        return d + sum(days[:m-1])
        