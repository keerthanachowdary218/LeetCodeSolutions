class Solution(object):
    def countCompleteComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        graph = [[] for _ in range(n)]
        for from_node, to_node in edges:
            graph[from_node].append(to_node)
            graph[to_node].append(from_node)
        visited = [False] * n
        def dfs(node, component):
            visited[node] = True
            component.append(node)
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor, component)
        def is_complete(component):
            for node in component:
                if len(graph[node]) != len(component) - 1:
                    return False
            return True
        ans = 0
        for node in range(n):
            if not visited[node]:
                component = []
                dfs(node, component)
                if is_complete(component):
                    ans += 1
        return ans
        