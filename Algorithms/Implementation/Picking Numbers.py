n = int(input())
a = list(map(int, input().split()))

maxCountOverall = 0
for num1 in a:

    list1 = list(filter(lambda x: 1 >= num1 - x >= 0, a))
    list2 = list(filter(lambda x: -1 <= num1 - x <= 0, a))

    if len(list1) > len(list2):
        maxCountHere = len(list1)
    else:
        maxCountHere = len(list2)

    if maxCountHere > maxCountOverall:
            maxCountOverall = maxCountHere

print(maxCountOverall)
    
