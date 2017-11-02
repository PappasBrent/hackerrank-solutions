t = int(input())

for i in range(t):
    n, k = map(int, input().split())
    aTimes = list(map(int, input().split()))

    count = 0
    for j in aTimes:
        if j <= 0:
            count += 1
    
    if count < k:
        print('YES')
    else:
        print('NO')
