# This works, but not for large lists

# import itertools

# n = int(input())

# a = list(map(int, input().split()))

# a.sort()

# aCombos = set(itertools.combinations(a, 2))

# def calc_pair_distance(pair):
#     return abs(pair[0] - pair[1])


# minDiff = abs(min(aCombos, key = calc_pair_distance)[0] - min(aCombos, key = calc_pair_distance)[1])

# # print(minDiff)

# answers = []

# for combo in aCombos:
#     if calc_pair_distance(combo) <= minDiff:
#         for i in combo:
#             answers.append(i)

# answers.sort()

# print(*answers)

# This is much more efficient

n = int(input())

a = list(map(int, input().split()))

a.sort()

minDiff = a[1] - a[0]

results = [a[0], a[1]]

for i in range(1, len(a) - 1):
    if a[i + 1] - a[i] < minDiff:
        minDiff = abs(a[i + 1] - a[i])
        results = []
        results.append(a[i])
        results.append(a[i + 1])
    elif a[i + 1] - a[i] == minDiff:
        results.append(a[i])
        results.append(a[i + 1])

print(*results)
