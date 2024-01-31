class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits:
            if digits[-1]!=9:
                digits[-1]=digits[-1]+1
                return digits
            else:
                number = 0
                for digit in digits:
                     number = number*10 + digit
                number=number+1
                res = [int(x) for x in str(number)]
                return (res)
        else:
            return 1
        '''
        if digits:
            if digits[-1]!=9:
                digits[-1]=digits[-1]+1
            else:
                digits[-1]=0
                if len(digits)>1:
                    digits[len(digits)-2]=digits[len(digits)-2]+1
                else:
                    digits[len[n]]
        '''
        