s, n, m = map(int, input().split())

np = list(map(int, input().split()))

mp = list(map(int, input().split()))

np.sort()
mp.sort()
np = np[::-1]
mp = mp[::-1]

bigPrice=-1
while len(np) > 0 and len(mp) > 0:
    for i in mp:
        if np[0] + i <= s:
            if np[0] + i > bigPrice:
                bigPrice = np[0] + i
    for i in np:
        if mp[0] + i <= s:
            if mp[0] + i > bigPrice:
                bigPrice = mp[0] + i
    del np[0]
    del mp[0]

print(bigPrice)

# print(np)
# print(mp)

# print(np[0] + mp[0])
