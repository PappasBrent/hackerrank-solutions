from math import ceil, sqrt


def sum_of_digits(x):
    s = str(x)
    total = 0
    for digit in s:
        total += int(digit)
    return total


p = int(input())
q = int(input())

answers = []

for i in range(p, q + 1):
    l = 0
    r = 0
    if i < 10:
        if i == 1:
            answers.append(1)
            # print(1, end=' ')
        if i == 9:
            answers.append(9)
            # print(9, end=' ')
        continue
    squareString = str(i**2)
    lenSquareString = len(squareString)
    if len(squareString) % 2 == 0:
        l = int(squareString[:int(lenSquareString / 2)])
        r = int(squareString[int(lenSquareString / 2):])
    else:
        l = int(squareString[:ceil(lenSquareString / 2) - 1])
        r = int(squareString[int(lenSquareString / 2):])
    # print(i, squareString, l, r)
    if l + r == i:
        answers.append(i)
        # print(i, end=' ')

if len(answers) != 0:
    print(*answers)
else:
    print("INVALID RANGE")