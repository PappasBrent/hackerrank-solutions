t = int(input())

for i in range(t):
    m = int(input())
    n = int(input())

    c = list(map(int, input().split()))

    affordableCosts = list(filter(lambda x: m - x > 0, c))

    for cost in affordableCosts:
        if m - cost in affordableCosts:
            cost1Index = c.index(cost) + 1
            if c.count(m - cost) >= 2 or m - cost == cost:
                c2 = c[:]
                c2.remove(cost)
                if m - cost in c2:
                    cost2Index = c2.index(m - cost) + 2
                    break
            else:
                cost2Index = c.index(m - cost) + 1
                break

    print(cost1Index, cost2Index)
