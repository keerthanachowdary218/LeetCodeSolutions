class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        min_freq = Counter(words[0])
        #print(min_freq)
        for word in words:
            min_freq &= Counter(word)
            #print(min_freq,word)
        return list(min_freq.elements())