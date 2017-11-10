n, m = map(int, input().split())

# c = [0 for x in range(n)]

maxDistance = -1

spaceStations = list(map(int, input().split()))

spaceStations.sort()

# print(*spaceStations)

for i in range(1, len(spaceStations)):
    if int((spaceStations[i] - spaceStations[i - 1]) / 2) > maxDistance:
        maxDistance = int((spaceStations[i] - spaceStations[i - 1]) / 2)

if n - spaceStations[-1] - 1 > maxDistance:
    maxDistance = n - spaceStations[-1] - 1

if spaceStations[0] - 0 > maxDistance:
    maxDistance = spaceStations[0] - 0

print(maxDistance)
