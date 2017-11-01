n, m = map(int, input().split())

a = list(map(int, input().split()))

b = list(map(int, input().split()))

total = 0

startingPoint=0
if min(a) <= min(b):
    startingPoint = min(a)
else:
    startingPoint = min(b)

endingPoint = 0
if max(a) > max(b):
    endingPoint = max(a)
else:
    endingPoint = max(b)

for i in range(startingPoint, endingPoint+1):

    xa = list(filter(lambda x: i % x == 0, a))
    xb = list(filter(lambda x: x % i == 0, b))

    if len(xa) == len(a) and len(xb) == len(b):
        total += 1


print(total)
