class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        count=Counter(t)
        for i in s:
            count[i]-=1
            if count[i]==0:
                del count[i]
        print(count)
        return list(count.keys())[0]

        