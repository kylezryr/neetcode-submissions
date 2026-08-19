class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = []
        freqMap = {}
        result = []

        for i in range(len(nums)+1):
            buckets.append([])
        
        # construct buckets and count frequencies
        for i in range(len(nums)):
            if nums[i] in freqMap:
                freqMap[nums[i]] = freqMap.get(nums[i]) + 1
            else:
                freqMap[nums[i]] = 1

        # place items into buckets
        for num in freqMap.items():
            buckets[num[1]].append(num[0])

        # retrieve top k items
        returnedSoFar = 0
        for j in range(len(buckets)-1, 0, -1):
            if returnedSoFar == k:
                break
            if len(buckets[j]) != 0:
                result.extend(buckets[j])
                returnedSoFar += len(buckets[j])

        return result