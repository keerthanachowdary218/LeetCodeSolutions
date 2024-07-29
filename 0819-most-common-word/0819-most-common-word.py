class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        k = "!?',;."
        s = paragraph.lower()
        for char in k:
            s = s.replace(char, ' ')
        co = dict(Counter(s.split()))
        sortedco=sorted(co.items(), key=lambda item: item[1],reverse=True)
        print(sortedco)
        for i in sortedco:
            if i[0] not in banned:
                return i[0]
        
        