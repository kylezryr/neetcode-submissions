class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        count = 0
        start = 0

        while count < n:
            current = start
            prev = nums[start]
            while True:
                temp = nums[(current + k) % n]
                nums[(current + k) % n] = prev
                prev = temp
                current = (current + k) % n
                count += 1

                if start == current:
                    break
            start += 1

            
            
