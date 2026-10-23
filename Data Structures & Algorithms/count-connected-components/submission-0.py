class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        # build adjList
        adjList = {i: [] for i in range(n)}
        for edge in edges:
            start = edge[0]
            end = edge[1]
            adjList[start].append(end)
            adjList[end].append(start)

        visited = set()
        count = 0

        def dfs(i):
            visited.add(i)

            for neighbor in adjList[i]:
                if neighbor not in visited:
                    dfs(neighbor)
        
        for node in range(n):
            if node not in visited:
                dfs(node)
                count += 1
            
        return count