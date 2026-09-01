class Solution:
    def trap(self, height: List[int]) -> int:
        prefixMax = [0] * len(height)
        suffixMax = [0] * len(height)
        water = [0] * len(height)

        # build prefixMax
        maxSoFar = height[0]
        for i in range(len(height)):
            if height[i] > maxSoFar:
                prefixMax[i] = height[i]
                maxSoFar = height[i]
            else:
                prefixMax[i] = maxSoFar
        
        # build suffixMax
        maxSoFar = height[-1]
        for j in range(len(height)-1, -1, -1):
            if height[j] > maxSoFar:
                suffixMax[j] = height[j]
                maxSoFar = height[j]
            else:
                suffixMax[j] = maxSoFar

        # iterate through list and find water at each position
        for k in range(len(height)):
            water[k] = min(prefixMax[k], suffixMax[k])-height[k]

        return sum(water)

        