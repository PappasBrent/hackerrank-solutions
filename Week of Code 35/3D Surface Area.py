
h, w = map(int, input().split())

board = [[] for y in range(h)]

for i in range(h):
    board[i] = list(map(int, input().split()))

print(*board, sep='\n')

total = 0

# Bottom of board
total += w**2

# Top of board
total += w**2

# Differences in heights of cubes
for i in range(w-1):
    for j in range(w-1):
        # To the right
        if (board[i][j] < board[i][j+1]):
            total += board[i][j + 1] - board[i][j]
        # To the left

        # Below
        if (board[i][j] < board[i + 1][j]):
            total += board[i + 1][j] - board[i][j]
        # Above
        

# Add the sides of the board

for i in range(w):
    # Top / Bottom
    total += board[0][i]
    total += board[-1][i]

    # Left / Right
    total += board[i][0]
    total += board[i][-1]
        
        

print(total)
