n, m, k = map(int, input().split())

grid = [[0 for x in range(n)] for y in range(n)]

grid[0][0] = m

for i in range(1, n):
    grid[i][i] = grid[i - 1][i - 1] + k

for i in range(n):
    for j in range(i+1, n):
        grid[i][j] = grid[i][j - 1] - 1

for j in range(n):
    for i in range(j + 1, n):
        grid[i][j] = grid[i - 1][j] - 1


for row in grid:
    print(*row, end='\n')

