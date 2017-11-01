n, k = map(int, input().split())


prices = list(map(int, input().split()))

cost = 0
numToys = 0

while (cost < k):
    cost+=min(prices)
    prices.remove(min(prices))
    if cost>k:
        break
    numToys+=1

print(numToys)