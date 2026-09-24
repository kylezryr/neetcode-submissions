class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        p1 = 0
        p2 = 0
        median1 = 0
        median2 = 0
        n1 = len(nums1)
        n2 = len(nums2)

        for _ in range((n1 + n2) // 2 + 1):
            median2 = median1
            if p1 < n1 and p2 < n2:
                if nums1[p1] > nums2[p2]:
                    median1 = nums2[p2]
                    p2 += 1
                else:
                    median1 = nums1[p1]
                    p1 += 1
            elif p1 < n1:
                median1 = nums1[p1]
                p1 += 1
            else:
                median1 = nums2[p2]
                p2 += 1

        if (n1 + n2) % 2 == 1:
            return float(median1)
        else:
            return (median1 + median2) / 2