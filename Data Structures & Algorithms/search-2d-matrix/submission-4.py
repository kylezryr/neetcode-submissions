class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix) # num rows
        n = len(matrix[0]) # num cols
        left = 0
        right = m - 1

        # one binary search to find row
        while left <= right:
            middle = (left + right) // 2
            row = matrix[middle]

            if (target in row):
                return True
            elif (row[0] > target):
                right = middle - 1
            elif(row[-1] < target):
                left = middle + 1
            else:
                break

        return False


        # one binary search to find column within row?


