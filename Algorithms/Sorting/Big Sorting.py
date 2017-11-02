from collections import defaultdict

n = int(input())

bucket = defaultdict(list)

for i in range(n):
    newNum  = input()
    bucket[len(newNum)].append(newNum)

for key in sorted(bucket):
    for val in sorted(bucket[key]):
        print(val)