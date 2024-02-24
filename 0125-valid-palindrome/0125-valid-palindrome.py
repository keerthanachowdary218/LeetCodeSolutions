class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1
        while l<r:
            if not s[l].isalnum():
                l=l+1
            if not s[r].isalnum():
                r=r-1
            if s[l].isalnum() and s[r].isalnum():
                if s[l].lower()==s[r].lower():
                    l=l+1
                    r=r-1
                else:
                    return False 
        return True
                
                    
                    
            
        