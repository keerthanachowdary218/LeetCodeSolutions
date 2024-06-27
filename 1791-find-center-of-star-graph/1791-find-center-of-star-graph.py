class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        hashh={}
        for edge in edges:
            if edge[0] in hashh:
                hashh[edge[0]]+=1
            else:
                hashh[edge[0]]=1
            if edge[1] in hashh:
                hashh[edge[1]]+=1
            else:
                hashh[edge[1]]=1
        for i in hashh:
            if hashh[i]==len(edges):
                return i
        