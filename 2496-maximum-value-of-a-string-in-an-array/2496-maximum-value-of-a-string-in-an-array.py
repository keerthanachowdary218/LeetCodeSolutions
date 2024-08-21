class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        value=0
        for strr in strs:
            if strr.isnumeric():
                value=max(value,int(strr))
            else:
                value=max(value,len(strr))
        return value
            
        