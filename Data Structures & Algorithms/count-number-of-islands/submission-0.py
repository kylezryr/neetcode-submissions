class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # go through all rows and columns
        # when you encounter a 1, dfs on neighboring cells
        # mark island as visited

        def dfs(r, c):
            if grid[r][c] == "0":
                return

            # mark island as visited
            grid[r][c] = "0"

            # out of bound check for neighbors
            if r > 0:
                dfs(r-1, c)
            if r < rows - 1:
                dfs(r+1, c)
            if c > 0:
                dfs(r, c-1)
            if c < cols - 1:
                dfs(r, c+1)

        rows = len(grid)
        cols = len(grid[0])
        count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "0":
                    continue
                
                # island found
                count += 1
                dfs(r, c)
        
        return count

