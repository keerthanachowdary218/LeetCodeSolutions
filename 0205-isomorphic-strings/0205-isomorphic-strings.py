class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        smap={}
        for i in range(0,len(s)):
            if s[i] in smap:
                smap[s[i]].append(i)
            else:
                smap[s[i]] = [i]
        print(smap.values())
        tmap={}
        for i in range(0,len(t)):
            if t[i] in tmap:
                tmap[t[i]].append(i)
            else:
                tmap[t[i]] = [i]
        print(tmap.values())
        #cant directly compare tmap.values() and smap.values()- its giving false. so convert to list and then compare
        values1 = list(smap.values())
        values2 = list(tmap.values())
        if values1==values2:
            return True
        else:
            return False
        

        