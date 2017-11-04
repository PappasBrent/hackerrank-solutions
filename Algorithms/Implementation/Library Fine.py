dr, mr, yr = map(int, input().split())

de, me, ye = map(int, input().split())

if yr < ye:
    cost = 0
elif yr == ye:
    if mr < me:
        cost = 0
    elif mr == me:
        if dr < de:
            cost = 0
        elif dr == de:
            cost = 0
        elif dr > de:
            cost = (dr - de) * 15
    elif mr > me:
        cost = (mr - me) * 500
elif yr > ye:
    cost = 10000

print(cost)