grid = []

for i in range(3):
    grid.append(list(map(int, input().split())))

for row in range(len(grid)):
    print('Row {0}: {1}'.format(row + 1, sum(grid[row])))

for row in range(len(grid)):
    print('Col {0}: {1}'.format(row + 1, grid[row][0] + grid[row][1] + grid[row][2]))

print('Diagonal LR: {0}'.format(grid[0][0]+grid[1][1]+grid[2][2]))

print('Diagonal RL: {0}'.format(grid[2][0] + grid[1][1] + grid[0][2]))
