class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        for i in items2:
            items1.append(i)
        items1.sort()
        i=0
        res=[]
        while i<len(items1):
            if i<(len(items1)-1) and items1[i][0]==items1[i+1][0]:
                res.append([items1[i][0],items1[i][1]+items1[i+1][1]])
                i=i+1
            else:
                res.append([items1[i][0],items1[i][1]])
            i+=1
        return (res)
        '''
        #below is using hashmap
        a, c, b =  defaultdict(int), [], items1 + items2
        for j in b:
            if j[0] not in a:  a[j[0]] = j[1]
            else: a[j[0]] = a[j[0]] + j[1]
        for i in sorted(a): c.append([i,a[i]])
        return c
        '''