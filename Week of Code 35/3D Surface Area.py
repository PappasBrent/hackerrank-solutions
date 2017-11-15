
h, w = map(int, input().split())

board = [[] for y in range(h)]

for i in range(h):
    board[i] = list(map(int, input().split()))

total = 0

# Bottom of board
total += w*h

# Top of board
total += w*h

# Differences in heights of cubes

# Right
for row in board:
    for i in range(len(row) - 1):
        if row[i] < row[i + 1]:
            total+=row[i + 1] - row[i]

# Left
for row in board:
    for i in range(len(row) - 1, 0, -1):
        if row[i] < row[i - 1]:
            total += row[i - 1] - row[i]

# Below
for i in range(h - 1):
    for j in range(w):
        if board[i][j] < board[i+1][j]:
            total += board[i+1][j] - board[i][j]

# Above
for i in range(h - 1, 0, -1):
    for j in range(w):
        if board[i][j] < board[i-1][j]:
            total+=board[i-1][j] - board[i][j]
        


# Adds the top / bottom sides of the board
total += sum(board[0])
total += sum(board[-1])


# Adds the left / right sides of the board
for i in range(h):
    # Left / Right
    total += board[i][0]
    total += board[i][-1]

        

print(total)
