class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        weaker = set()
        stronger = []

        # all destinations are weaker nodes
        for edge in edges:
            weaker.add(edge[1])
        
        for i in range(n):
            if i not in weaker:
                stronger.append(i)

        if len(stronger) == 1:
            return stronger[0]
        else:
            return -1
        