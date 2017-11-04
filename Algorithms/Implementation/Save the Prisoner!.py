t = int(input())

for i in range(t):
    n, m, s = map(int, input().split())

    numFromStart = m + s - 1

    finalPos = numFromStart % n

    if finalPos == 0:
        print(n)
    else:
        print(finalPos)