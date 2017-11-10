t = int(input())

for _ in range(t):
    n = int(input())

    gridNormal = [[] for row in range(n)]

    for i in range(n):
        for letter in input():
            gridNormal[i].append(letter)

    for i in range(n):
        gridNormal[i].sort()
        gridNormal[i] = ''.join(gridNormal[i])

    gridIdeal = gridNormal[:]
    gridIdeal.sort()

    # print()

    # print(*gridNormal, sep='\n', end='\n\n')
    # print(*gridIdeal, sep='\n', end='\n\n')

    if gridNormal == gridIdeal:

        allVertsMatch = True
        for i in range(n):
            vertStringNormal = []
            for j in range(n):
                vertStringNormal.append(gridNormal[j][i])

            vertStringIdeal = vertStringNormal[:]
            vertStringIdeal.sort()
            vertStringNormal = ''.join(vertStringNormal)
            vertStringIdeal = ''.join(vertStringIdeal)
            # print(vertStringNormal, vertStringIdeal)
            if vertStringNormal == vertStringIdeal:
                pass
            else:
                allVertsMatch = False
                break
        
        if allVertsMatch:
            print('YES')
        else:
            print('NO')

    else:
        print('NO')
