class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        #print(s.split())
        return ' '.join(word[::-1] for word in s.split())


        