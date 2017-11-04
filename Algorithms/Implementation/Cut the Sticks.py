n = int(input())

sticks = list(map(int, input().split()))

while len(sticks) > 0:
    print(len(sticks))
    smallestStick = min(sticks)
    for i in range(len(sticks)):
        sticks[i] -= smallestStick
    sticks = list(filter(lambda x: x > 0, sticks))