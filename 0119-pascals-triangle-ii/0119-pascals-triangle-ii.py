class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        #using zip
        for i in range(1, rowIndex + 1):
            row=[l+r for l,r in zip([0]+row,row+[0])]
        return row