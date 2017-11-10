t = int(input())

for _ in range(t):
    s1 = 0
    n = int(input())
    a = int(input())
    b = int(input())

    print(*range(a, n, a))
    print(*range(b, n, b))
    