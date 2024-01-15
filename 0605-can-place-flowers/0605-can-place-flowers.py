class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count=0
        if len(flowerbed)==1 and flowerbed[0]==0:
            return True
        for i in range(0,len(flowerbed)):
            if flowerbed[i]==0:
                print(i)
                if i==0:
                    if i<=(len(flowerbed)-2):
                        if flowerbed[i+1]==0:
                            count=count+1
                            flowerbed[i]=1
                if i==(len(flowerbed)-1):
                    if i>1:
                        if flowerbed[i-1]==0:
                            count=count+1
                            flowerbed[i]=1
                if i>=1 and i<=(len(flowerbed)-2):
                    if flowerbed[i]==0 and flowerbed[i-1]==0 and flowerbed[i+1]==0:
                        count=count+1
                        flowerbed[i]=1
        if count>=n:
            return True
        else:
            return False
        