n = int(input())

grid = [input() for row in range(n)]

newGrid = [[] for row in range(n)]

for i in range(n):
    for digit in grid[i]:
        newGrid[i].append(digit)

# print(*grid, sep="\n")

# print()

# print(*newGrid, sep='\n')

for row in range(n):
    for col in range(n):
        if 0 < row < n - 1:
            if 0 < col < n - 1:
                currentNum = int(grid[row][col])
                leftNum = int(grid[row][col - 1])
                rightNum = int(grid[row][col + 1])
                bottomNum = int(grid[row+1][col])
                topNum = int(grid[row-1][col])

                if currentNum > leftNum and currentNum > rightNum and currentNum > bottomNum and currentNum > topNum:
                    newGrid[row][col] = 'X'
                # print(currentNum)


for i in range(n):
    newGrid[i] = ''.join(newGrid[i])


print(*newGrid, sep='\n')