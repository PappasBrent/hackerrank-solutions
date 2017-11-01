n, k = map(int, input().split())

c = tuple(map(int, input().split()))

b = int(input())

if (sum(c) / 2) == b:
    print(int(b - ((sum(c) - c[k]) / 2)))
else:
    print("Bon Appetit")
