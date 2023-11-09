class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        flag=0
        for i in range(0,n-1):
            if prices[i]<prices[i+1]:
                flag=1
                break
        if flag==0:
            return 0
        else:
            if n>=1:
                diff=0
                maxi=0
                i=0
                j=i+1
                while(i<j and i<n and j<n and i!=j):
                    #print(i,j)
                    diff=prices[j]-prices[i]
                    if(diff<=0):
                        i=j
                        j=j+1
                    elif(maxi<=diff):
                        maxi=diff
                        j=j+1
                    elif(maxi>diff):
                        j=j+1
                return maxi
            else:
                return 0
                
                
            