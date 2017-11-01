n = int(input())

s = input()

total = 0
y = 0

for c in s:
    if c == 'U':
        y += 1
        if y == 0:
            total += 1
    if c == 'D':
        y-=1

print(total)