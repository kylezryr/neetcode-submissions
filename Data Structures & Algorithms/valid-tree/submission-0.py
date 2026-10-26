class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # cycle detection and all nodes are connected
        adjList = {i: [] for i in range(n)}
        for source, dest in edges:
            adjList[source].append(dest)
            adjList[dest].append(source)
        
        visited = set()
        def dfs(node, parent):
            visited.add(node)

            for neighbor in adjList[node]:
                if neighbor not in visited:
                    # cycle detected in neighbor
                    if not dfs(neighbor, node):
                        return False
                # encountered a visited node that's not the parent -- cycle
                elif neighbor != parent:
                    return False

            return True

        noCycle = dfs(0, 0)
        if len(visited) == n and noCycle:
            return True
        else:
            return False