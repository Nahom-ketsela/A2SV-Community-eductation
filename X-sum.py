def x_sum(grid, n, m):
    max_sum = 0
    
    for i in range(n):
        for j in range(m):
            current_sum = 0
 
            for k in range(min(n, m)):
                if i - k >= 0 and j - k >= 0:  # ↖ (up-left)
                    current_sum += grid[i - k][j - k]
                if i - k >= 0 and j + k < m:  # ↗ (up-right)
                    current_sum += grid[i - k][j + k]
                if i + k < n and j - k >= 0:  # ↙ (down-left)
                    current_sum += grid[i + k][j - k]
                if i + k < n and j + k < m:  # ↘ (down-right)
                    current_sum += grid[i + k][j + k]
                
            # Remove the cell (i, j) three times because it has been added four times
            current_sum -= 3 * grid[i][j]
            max_sum = max(max_sum, current_sum)
    
    return max_sum
 
# Input handling
t = int(input())
results = []
 
for _ in range(t):
    n, m = map(int, input().split())
    grid = []
    for i in range(n):
        grid.append(list(map(int, input().split())))
    
    results.append(x_sum(grid, n, m))
 
for result in results:
    print(result)
