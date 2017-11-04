n = int(input())

c = list(map(int, input().split()))

count = 0
p = 0

while p < len(c) - 1:
    if p + 2 <= len(c) - 1 and c[p + 2] != 1:
        p += 2
    else:
        p += 1
    count += 1

print(count)
