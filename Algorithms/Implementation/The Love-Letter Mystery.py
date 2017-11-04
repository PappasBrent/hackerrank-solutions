t = int(input())

for i in range(t):
    s = input()
    numOperations = 0
    midPoint = int(len(s) / 2)
    firstHalf = s[:midPoint]
    if len(s) % 2 != 0:
        secondHalf = s[midPoint + 1:]
    else:
        secondHalf = s[midPoint:]
    secondHalf = secondHalf[::-1]

    for i in range(len(firstHalf)):
        numOperations += abs(ord(firstHalf[i]) - ord(secondHalf[i]))

    # print(firstHalf, secondHalf, numOperations)

    print(numOperations)
