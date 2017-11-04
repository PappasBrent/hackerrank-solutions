n = int(input())

currentDayTotal = 5

total = 0

i = 0

while (i < n):
    currentDayTotal = int(currentDayTotal / 2)
    total += currentDayTotal
    currentDayTotal *= 3
    i+=1

print(total)
