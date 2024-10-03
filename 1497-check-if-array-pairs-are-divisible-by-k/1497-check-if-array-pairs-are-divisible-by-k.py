class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        hashh={}
        for i in arr:
            if i%k in hashh:
                hashh[i%k].append(i)
            else:
                hashh[i%k]=[i]
        #print(hashh)
        for i in range(0,k):
            #print(i)
            if i in hashh:
                #print(i)
                if i==0:
                    if len(hashh[i])%2!=0:
                        return False
                elif len(hashh.get(i, [])) != len(hashh.get(k - i, [])):
                        return False
        return True
            
               
            
        