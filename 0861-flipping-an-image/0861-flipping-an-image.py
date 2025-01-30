class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        newimage=[]
        for row in image:
            newrow=[]
            for i in row[::-1]:
                if i==0:
                    newrow.append(1)
                else:
                    newrow.append(0)
            newimage.append(newrow)
        return newimage
        