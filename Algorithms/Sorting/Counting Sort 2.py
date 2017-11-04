n = int(input())

a = [0 for x in range(100)]

nums = list(map(int, input().split()))

for i in range(100):
    a[i] = nums.count(i)

for i in range(100):
    for j in range(a[i]):
        print(i, end=' ')