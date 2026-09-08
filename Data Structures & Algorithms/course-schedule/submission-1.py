class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build graph adjacency list
        adjMap = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            adjMap[course].append(pre)

        visiting = set()

        def dfs(node):
            if node in visiting:
                return False
            if adjMap[node] == []:
                return True

            visiting.add(node)
            for pre in adjMap[node]:
                if not dfs(pre):
                    return False
            visiting.remove(node)
            adjMap[node] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True