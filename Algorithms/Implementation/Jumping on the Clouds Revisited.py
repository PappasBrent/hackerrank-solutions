n, k = map(int, input().split())
c = list(map(int, input().split()))
i = 0
E = 100

i = (i + k) % n
E -= (3**c[i])

while i != 0:
    i = (i + k) % n
    E -= (3**c[i])

print(E)
