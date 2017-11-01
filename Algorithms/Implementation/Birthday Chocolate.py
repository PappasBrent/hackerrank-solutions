n = int(input())

pieces = list(map(int, input().split()))

d, m = map(int, input().split())

total = 0

for i in range(n - m + 1):
    # print(*pieces[i:i+m])
    if sum(pieces[i:i+m]) == d:
        total+=1

print(total)