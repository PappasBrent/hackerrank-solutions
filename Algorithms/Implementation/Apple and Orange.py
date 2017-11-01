s, t = map(int, input().split())

a, b = map(int, input().split())

m, n = map(int, input().split())

apples = list(map(int, input().split()))

oranges = list(map(int, input().split()))

count = 0

for apple in apples:
    if a + apple >= s and a + apple <= t:
        count += 1

print(count)

count = 0

for orange in oranges:
    if b + orange >= s and b + orange <= t:
        count += 1

print(count)