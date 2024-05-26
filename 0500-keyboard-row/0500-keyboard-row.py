class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1='qwertyuiop'
        row2='asdfghjkl'
        row3='zxcvbnm'
        res=[]
        for word in words:
            if word[0].lower() in row1:
                count=0
                for i in word.lower():
                    if i not in row1:
                        break
                    else:
                        count+=1
                if count==len(word):
                    res.append(word)
            elif word[0].lower() in row2:
                count=0
                for i in word.lower():
                    if i not in row2:
                        break
                    else:
                        count+=1
                if count==len(word):
                    res.append(word)
            else:
                count=0
                for i in word.lower():
                    if i not in row3:
                        break
                    else:
                        count+=1
                if count==len(word):
                    res.append(word)
        return res
    '''
    #using sets- no need for nested loop
    l1="qwertyuiop"
    l2="asdfghjkl"
    l3="zxcvbnm"
    res=[]
    for word in words:
        w=word.lower()
        if len(set(l1+w))==len(l1) or len(set(l2+w))==len(l2) or len(set(l3+w))==len(l3) :
            res.append(word)
    return res
    '''
                   
        
        