import sys

n = int(input())

scores = list(map(int, input().split()))

lowInc = 0
highInc = 0

lowest = scores[0]
highest = scores[0]

for score in scores:
    if score < lowest:
        lowInc += 1
        lowest = score
    elif score > highest:
        highInc += 1
        highest = score

print(highInc, lowInc)