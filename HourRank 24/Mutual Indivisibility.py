t = int(input())

for i in range(t):
    a, b, x = map(int, input().split())

    possibleNums = list(range(a, b + 1))

    for i in range(a, b + 1):
        for j in possibleNums:
            if j != i:
                if j % i == 0:
                    if i in possibleNums:
                        possibleNums.remove(i)

    if len(possibleNums) < x:
        print(-1)
    else:
        print(*possibleNums)
