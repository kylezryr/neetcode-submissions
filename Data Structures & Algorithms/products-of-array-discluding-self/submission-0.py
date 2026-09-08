class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefixProds = [0] * n
        suffixProds = [0] * n
        result = [0] * n

        currentProd = 1
        for i in range(n):
            currentProd = currentProd * nums[i]
            prefixProds[i] = currentProd

        currentProd = 1
        for j in range(n - 1, -1, -1):
            currentProd = currentProd * nums[j]
            suffixProds[j] = currentProd

        for k in range(n):
            prefix = prefixProds[k-1] if k > 0 else 1
            suffix = suffixProds[k+1] if k < n - 1 else 1

            product = prefix * suffix
            result[k] = product

        return result

