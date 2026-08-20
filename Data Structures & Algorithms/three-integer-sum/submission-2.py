class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort array in ascending order
        sortedArray = sorted(nums)
        result = []
        n = len(sortedArray)

        for i in range(n-2):
            if i>0 and sortedArray[i] == sortedArray[i-1]:
                continue
            left = i+1
            right = n-1
            while left < right:
                currSum = sortedArray[i] + sortedArray[left] + sortedArray[right]
                if currSum == 0:
                    triplet = [sortedArray[i], sortedArray[left], sortedArray[right]]
                    if triplet not in result:
                        result.append(triplet)
                    left += 1
                    right -= 1
                elif currSum < 0:
                    # too small, bring left up
                    left += 1
                else:
                    # too big, bring right down
                    right -= 1
        
        return result