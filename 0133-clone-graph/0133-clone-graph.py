"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #copy the each node and make sure you are not creating the duplicate value
        #for that we will be using hashmap
        if not node:
            return None
        visited = {}
        queue = deque([node])
        visited[node] = Node(node.val)
        while queue:
            # Get the next node from the queue
            curr_node = queue.popleft()
            for neighbor in curr_node.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                visited[curr_node].neighbors.append(visited[neighbor])
        return (visited[node])        