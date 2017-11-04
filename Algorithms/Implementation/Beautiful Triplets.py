n, d = map(int, input().split())

a = list(map(int, input().split()))

count = 0

# Slower

# for j in range(1, len(a) - 1):
#     for i in range(j):
#         if a[j] - a[i] == d:
#             for k in range(j + 1, len(a)):
#                 if a[k] - a[j] == d:
#                     count += 1


# Feasible
for i in range(len(a)):
    if a[i] + d in a and a[i] + 2 * d in a:
        count += 1

print(count)
