i, j, k = map(int, input().split())

count = 0

for num in range(i, j + 1):
    if abs(num - int(str(num)[::-1])) % k == 0:
        count += 1

print(count)
