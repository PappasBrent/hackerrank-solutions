n = int(input())

ar = list(map(int, input().split()))

e = ar[-1]

index = -2

while ar[index] > e:
    e = ar[-1]

index = -2

while ar[index] > e:
    ar[index + 1] = ar[index]
    for item in ar:
        print(item, end=' ')
    index -= 1
    if index < -1 * len(ar):
        print()
        break
    print()

ar[index + 1] = e

ar[index + 1] = e

for item in ar:
    print(item, end=' ')
