class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        island_count = 0

        def dfs(r, c):
            # Base case: out of bounds or water
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
                return

            # Mark the cell as visited
            grid[r][c] = '0'

            # Explore neighbors (up, down, left, right)
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Iterate through the grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    # Found a new island
                    island_count += 1
                    # Explore the island using DFS
                    dfs(r, c)

        return island_count