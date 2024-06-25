class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        hashh={}
        alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        currnt=0
        for i in range(0,len(key)):
            if key[i] not in hashh and key[i]!=' ':
                #print(key[i])
                hashh[key[i]]=alpha[currnt]
                currnt+=1
        #print(hashh)
        res=''
        for i in message:
            if i==' ':
                res+=i
            else:
                res+=hashh[i]
        return res