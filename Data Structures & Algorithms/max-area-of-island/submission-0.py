class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        best = 0

        def dfs(r, c) -> int:
            island_area = 0
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != 1:
                return 0
            grid[r][c] = 0
            island_area = dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1) + 1
            return island_area


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    best = max(best, dfs(r, c))
        return best

# rows, cols; best = 0

# dfs(r, c) returns the size of the island starting here
    # STOP: off grid or not land (== 1)? return 0
    # MARK: grid[r][c] = 0
    # RECURSE: return 1 + dfs(down) + dfs(up) + dfs(right) + dfs(left)

# for each r, c
    # if grid[r][c] == 1:
        # best = max(best, dfs(r, c))
# return best
