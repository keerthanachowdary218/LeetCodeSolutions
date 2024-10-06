class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        words1 = sentence1.split()
        words2 = sentence2.split()
        if len(words1) < len(words2):
            words1, words2 = words2, words1
        start, end = 0, 0
        n1, n2 = len(words1), len(words2)
        while start < n2 and words1[start] == words2[start]:
            start += 1

        # Compare words from the end of both sentences
        while end < n2 and words1[n1 - end - 1] == words2[n2 - end - 1]:
            end += 1

        # Check if the remaining unmatched part is only in the middle
        return start + end >= n2
        