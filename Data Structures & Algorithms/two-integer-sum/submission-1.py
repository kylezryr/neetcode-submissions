class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # go through each element in list
        # check if there is any future element that is target - elem
        result = [0, 0]

        # build target - elem hash map 
        remaining = {}
        for i in range(len(nums)):
            remaining[nums[i]] = i

        for j in range(len(nums)):
            difference = target - nums[j]
            if difference in remaining:
                otherIndex = remaining.get(difference)
                if otherIndex != j:
                    result[0] = j
                    result[1] = otherIndex
                    return result
