from collections import Counter

sCounter = Counter(input())

# print(sCounter.most_common())

# print(sCounter.most_common()[-1])

if (sCounter.most_common()[0][1]) == sCounter.most_common()[-1][1]:
    print('YES')
else:
    if sCounter.most_common()[0][1] == sCounter.most_common()[-2][1] and sCounter.most_common()[-1][1]==1:
        print('YES')
        exit()
    if (sCounter.most_common()[0][1] - 1) == sCounter.most_common()[-1][1]:
        if sCounter.most_common()[0][1] == sCounter.most_common()[1][1]:
            print('NO')
        else:
            print('YES')
    else:
        print('NO')