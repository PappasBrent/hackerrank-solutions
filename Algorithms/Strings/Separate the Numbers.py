q = int(input())

for i in range(q):
    s = input()
    goodStartingNums = []
    for i in range(1, int(len(s) / 2) + 1):
        startingNum = int(s[:i])
        incNum = startingNum
        endingString = str(startingNum)
        while len(endingString) < len(s):
            endingString += str(incNum + 1)
            incNum += 1

        if(endingString == s):
            goodStartingNums.append(startingNum)

    if len(goodStartingNums) != 0:
        print('YES', goodStartingNums[0])
    else:
        print('NO')
