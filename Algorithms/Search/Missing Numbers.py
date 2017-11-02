input()
a = list(map(int, input().split()))
input()
b = list(map(int, input().split()))

missingNums = [0 for x in range(10001)]

for num in a:
    missingNums[num] -= 1

for num in b:
    missingNums[num] += 1

# In the end, if any number occurred an unequal amount of times in
# the two lists then its value sin missingNums should not equal 0
for i in range(len(missingNums)):
    if missingNums[i] != 0:
        print(i, end=' ')
