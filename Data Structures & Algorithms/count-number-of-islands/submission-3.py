class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        print(rows)
        cols = len(grid[0])
        print(cols)
        count = 0

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != '1':
                return
            grid[r][c] = '0'
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    dfs(r, c)
                    count += 1
        return count

        # Define rows bounds by grid length (how many lists in grid)
        # Define cols bounds by length of grid's first entry
        # Initialize counter variable to 0

        # Define a DFS function that takes arguments (r, c) (Rows and Columns) - Call it dfs(r, c)
            # The if portion here will determine whether position we are looking at is off the grid
            # If r is less than rows bounds or c is less than cols bounds or r greater than equal to rows or c is greater than equal to bounds or grid position (grid[r][c]) does not equal to 1
                # Exit function (Return)
            # Mark current position as visited (grid[r][c] = '0')
            # Call function dfs on 4 neighbors of current position
            # dfs(r + 1, c) Down
            # dfs(r - 1, c) Up
            # dfs(r, c + 1) Right
            # dfs(r, c - 1) Left

            # Iterate through the grid by rows and cols
            # For each r in range rows
                # For each c in range cols
                    # If position grid[r][c] is equal to 1, flood the island and increase count
                        # Call function dfs
                        # Increase count by one
            # Return count
