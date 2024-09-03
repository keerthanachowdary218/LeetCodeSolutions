class Solution:
    def getLucky(self, s: str, k: int) -> int:
        res=0
        for letter in s:
            num=ord(letter)-96
            if num<=9:
                res+=num
            else:
                #print((num//10) , (num%10))
                res+=(num//10) + (num%10)
        print(res)
        while k>=2:
            summ = 0
            for digit in str(res):  
                summ += int(digit)  
            res=summ
            k=k-1
        return res
            
        