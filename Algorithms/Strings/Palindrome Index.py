t = int(input())

for i in range(t):
    s = input()
    index = -1

    middleIndex = int(len(s) / 2)
    firstHalf = s[:middleIndex]
    secondHalf = s[middleIndex:]

    if len(s) % 2 != 0:
        firstHalf += s[middleIndex]

    secondHalf = secondHalf[::-1]
    print(firstHalf)
    print(secondHalf)

    for j in range(len(firstHalf)):
        if firstHalf[j] != secondHalf[j]:
            if str(s[:j] + s[j + 1:]) == str(s[:j] + s[j + 1:])[::-1]:
                index = j
            else:
                index = len(s) - j - 1
            break

    print(index)
