class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # build adj list
        adjList = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            adjList[prereq].append(course)

        visiting = set()
        visited = set()
        result = []

        def dfs(node):
            if node in visiting:
                return False
            if node in visited:
                return True

            visiting.add(node)
            for neighbor in adjList[node]:
                if neighbor not in visited:
                    if not dfs(neighbor):
                        return False
                
            visiting.remove(node)
            visited.add(node)
            result.append(node) # post order add node
            return True

        for i in range(numCourses):
            if i not in visited:
                if not dfs(i):
                    return [] # cycle detected, impossible

        result.reverse()
        return result