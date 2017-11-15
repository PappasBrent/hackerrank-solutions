import string

n = int(input())

lowestPrice = float("inf")
bestBrand = ''

for i in range(n):
    validPrice = True
    currentBrand, currentPrice = input().split()
    for digit in string.digits:
        if digit not in ['4', '7'] and currentPrice.count(digit) != 0:
            validPrice = False
            break
    if not validPrice:
        continue
    else:
        if currentPrice.count('4') != currentPrice.count('7'):
            validPrice = False
    if validPrice:
        if int(currentPrice) < lowestPrice:
            lowestPrice = int(currentPrice)
            bestBrand = currentBrand


if (bestBrand == ''):
    print(-1)
else:
    print(bestBrand)
