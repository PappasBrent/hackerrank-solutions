n, k = map(int, input().split())

maxHeight = max(list(map(int, input().split())))

numDrinks = maxHeight - k

if numDrinks < 0:
    numDrinks = 0

print(numDrinks)
