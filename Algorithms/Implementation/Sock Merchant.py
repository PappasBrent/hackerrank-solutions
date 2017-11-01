n = int(input())

c = list(map(int, input().split()))

total = 0

for i in range(1, 101):
    if i in c:
        if c.count(i) % 2 == 0:
            total += c.count(i) / 2
        else:
            total += (c.count(i) - 1) / 2

print(int(total))
