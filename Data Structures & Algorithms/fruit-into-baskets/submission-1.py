class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = defaultdict(int)
        left = 0
        result = 0
        total = 0

        for right in range(len(fruits)):
            count[fruits[right]] += 1
            total += 1

            while len(count) > 2:
                fruit = fruits[left]
                count[fruit] -= 1
                total -= 1
                left += 1
                if not count[fruit]:
                    count.pop(fruit)
        
            result = max(result, total)

        return result