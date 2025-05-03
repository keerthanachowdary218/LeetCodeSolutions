class Solution(object):
    def toGoatLatin(self, sentence):
        """
        :type sentence: str
        :rtype: str
        """
        words=sentence.split()
        print(words)
        res=''
        i=1
        for word in words:
            if word[0].lower() in 'aeiou':
                curr=word+'ma'
            else:
                curr=word[1:]+word[0]+'ma'
            res+=curr+'a'*i+' '
            i+=1
        return res.rstrip()

        