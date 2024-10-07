class Solution:
    def minLength(self, s: str) -> int:
        while True:
            if 'AB' in s:
                s=s.replace('AB','')
                print(s)
            elif 'CD' in s:
                s=s.replace('CD','')
                print(s)
            else:
                return len(s)
                
        