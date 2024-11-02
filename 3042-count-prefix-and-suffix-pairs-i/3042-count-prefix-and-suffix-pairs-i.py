class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(str1, str2):
            l=len(str1)
            if str2[:l]==str1 and str2[-l:]==str1:
                return True
            return False
        count=0
        i=0
        j=1
        for i in range(0,len(words)-1):
            for j in range(i,len(words)):
                if i<j and isPrefixAndSuffix(words[i], words[j]):
                    count+=1
        return count
        
        