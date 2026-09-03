class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])
        
        # reverse rows, first row becomes last row
        matrix.reverse()

        # iterate over upper right triangle and swap with lower left triangle
        for r in range(n):
            for c in range(r, m):
                if r == c:
                    continue

                temp = matrix[c][r]
                matrix[c][r] = matrix[r][c]
                matrix[r][c] = temp