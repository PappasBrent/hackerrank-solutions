for i in range(int(input())):
    n, c, m = map(int, input().split())
    count = w = n // c
    while w >= m:
        w -= m
        count += 1
        w += 1
    print(count)
