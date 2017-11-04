n = int(input())

a = list(map(int,input().split()))

minDist = 99999999999

for i in range(len(a)):
    indexOne = i
    if a[i] in a[i + 1:]:
        indexTwo = a[i + 1:].index(a[i])
        indexTwo += len(a[:i+1])
        thisMinDist = abs(indexOne - indexTwo)
        if thisMinDist < minDist:
            minDist = thisMinDist

if minDist != 99999999999:
    print(minDist)
else:
    print(-1)
