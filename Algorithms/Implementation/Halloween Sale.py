p, d, m, s = list(map(int, input().split()))

n = 0
c = 0
while c <= s:
    c += p
    p = p - d if p - d > m else m

    n += 1

print(n)