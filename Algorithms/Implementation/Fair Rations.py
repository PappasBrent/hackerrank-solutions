n = int(input())

b = list(map(int, input().split()))

if sum(b) % 2 != 0:
    print('NO')

else:
    count = 0
    total = 0
    for i in b:
        total += i
        if total % 2 != 0:
            count += 2
    
    print(count)
