for _ in range(int(input())):
    n = int(input())
    a = int(input())
    b = int(input())

    first = min(a, b) * (n - 1)
    last = max(a, b) * (n - 1)
    inc = (last-first) // (n-1)

    results = []
    if inc == 0:
        print(first)
    else:
        for i in range(n):
            results.append(first + (i * inc))
        print(*results)

'''
In: 3 1 2
Out: 2 3 4

In: 4 10 100
Out: 30 120 210 300

In: 73 25 25
Out: 

'''
