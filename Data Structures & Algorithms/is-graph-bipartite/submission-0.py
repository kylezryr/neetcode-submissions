class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = [-1] * len(graph)

        def dfs(node, color):
            colors[node] = color
            for neighbor in graph[node]:
                if colors[neighbor] == -1:
                    if not dfs(neighbor, 1 - color):
                        return False
                elif colors[neighbor] == colors[node]:
                    return False
            
            return True
        
        for node in range(len(graph)):
            if colors[node] == -1:
                if not dfs(node, 0):
                    return False
        
        return True