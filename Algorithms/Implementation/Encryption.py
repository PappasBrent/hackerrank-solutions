# My original method (doesn't quite work, but almost)

# import math

# s = input()

# s = s.replace(" ", '')

# numRows = math.floor(math.sqrt(len(s)))
# numCols = math.ceil(math.sqrt(len(s)))

# grid = [['' for col in range(numCols)] for row in range(numRows)]

# rowNo = 0
# colNo = 0

# while colNo < len(s) and rowNo < len(grid):

#     grid[rowNo][colNo % numCols] = s[colNo]
#     colNo += 1
#     if colNo != 0 and colNo % numCols == 0:
#         rowNo += 1

# print(*grid, sep='\n')

# phrase = ''

# for colNo in range(len(grid[0])):
#     for rowNo in range(len(grid)):
#         phrase += grid[rowNo][colNo]
#     phrase += ' '

# print(phrase.strip())

# Much better method (adjusted for my own readability)

from math import ceil, sqrt

s = input()
skip = ceil(sqrt(len(s)))
newWords = list(map(lambda x: s[x::skip], range(skip)))
print(*newWords)
