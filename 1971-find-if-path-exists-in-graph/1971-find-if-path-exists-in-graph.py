class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        visited=set()
        def findPath(start,end):
            if (start, end) in visited:
                return False
            visited.add((start, end))
            if ([start,end] in edges) or ([end,start] in edges):
                return True
            else:
                for i in edges:
                    if i[0]==start:
                        if findPath(i[1],end):
                            return True
                    elif i[1]==start:
                        if findPath(i[0],end):
                            return True
                return False
        if len(edges)==0:
            return True
        else:
            return findPath(source,destination)             
        