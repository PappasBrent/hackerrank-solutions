n = int(input())

a = list(map(int, input().split()))

p = a[0]

smallNums = []
bigNums = []
equalNums = []

for val in a:
    if val < p:
        smallNums.append(val)
    elif val == p:
        equalNums.append(val)
    elif val > p:
        bigNums.append(val)

print(*smallNums, *equalNums, *bigNums)
