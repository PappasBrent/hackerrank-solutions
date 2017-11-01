n = int(input())

p = int(input())

total = min([int(abs(n - p) / 2), int(abs(p) / 2)])

if n % 2 == 0 and p == n - 1 and p != 1:
    total+=1

print(total)
