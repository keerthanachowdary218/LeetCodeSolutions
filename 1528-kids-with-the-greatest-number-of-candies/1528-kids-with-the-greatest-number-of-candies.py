class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxi=max(candies)
        print(maxi)
        res=[]
        for i in (candies):
            if i+extraCandies>=maxi:
                res.append(True)
            else:
                res.append(False)
        return res
        