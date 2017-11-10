# WOO this was tough

from math import ceil

n, k = map(int, input().split())

numProblemsInChapters = list(map(int, input().split()))

numPagesInChapters = []

for numProblems in numProblemsInChapters:
    numPagesInChapters.append(ceil(numProblems / k))

chNum = 1

total = 0

while chNum - 1 < len(numPagesInChapters):
    if numProblemsInChapters[chNum - 1] >= sum(numPagesInChapters[:chNum]):

        # total += 1
        numPagesByEndOfCh = sum(numPagesInChapters[:chNum])
        numProblemsInThisChapter = numProblemsInChapters[chNum - 1]

        # print("Chapter number:", str(chNum), "Number of pages in total by the end of this chapter:", str(
            # numPagesByEndOfCh))

        currentProblemNo = 1
        currentPageNo = sum(
            numPagesInChapters[:chNum]) - numPagesInChapters[chNum - 1] + 1
        # print(currentPageNo)
        while currentPageNo <= numPagesByEndOfCh:
            # print("Current page number", str(currentPageNo), "Current problem number", str(currentProblemNo))
            if currentProblemNo == currentPageNo:
                # print("SPECIAL PROBLEM: PROBLEM", str(currentProblemNo), "@ PAGE", str(currentPageNo))
                total += 1
            if currentProblemNo % k == 0 or currentProblemNo >= numProblemsInThisChapter:
                currentPageNo += 1
            currentProblemNo += 1

    chNum += 1

# print()
print(total)
