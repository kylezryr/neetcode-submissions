class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 0:
            return 0
        if len(cost) == 1:
            return min(cost[0], cost[1])
        bestSoFar = [0] * len(cost)
        bestSoFar[0] = cost[0]
        bestSoFar[1] = cost[1]

        for i in range(2, len(cost)):
            print("bestSoFar before: ", bestSoFar)
            bestSoFar[i] = min(bestSoFar[i-2] + cost[i], bestSoFar[i-1] + cost[i])
            print("bestSoFar after: ", bestSoFar)

        return min(bestSoFar[-1], bestSoFar[-2])