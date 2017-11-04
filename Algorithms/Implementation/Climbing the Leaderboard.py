# n = int(input())

# scores = list(map(int, input().split()))

# m = int(input())

# aScores = list(map(int, input().split()))

# minRank = 2

# for aScore in aScores:

#     rank = minRank
#     if aScore >= scores[0]:
#         rank = 1
#     else:
#         for i in range(1, len(scores)):
#             prevNum = scores[i - 1]
#             if aScore < scores[i]:
#                 if scores[i] != prevNum:
#                     rank += 1
#                 else:
#                     continue
#             else:
#                 break
#     if rank > minRank:
#         minRank = rank
#     print(rank)

n = int(input())

scores = []

for score in map(int, input().split()):
    if score not in scores:
        scores.append(score)

m = int(input())

aScores = list(map(int, input().split()))

startIndex = 0

for aScore in aScores:

    # try:
    #     print(scores.index(next(score for score in scores if score <= aScore)) + 1)
    # except StopIteration:
    #     print(len(scores) + 1)

    i = startIndex

    newScores = scores[:]
    newScores.append(aScore)
    newScores.sort()
    newScores = newScores[::-1]
    print(newScores.index(aScore) + 1)
