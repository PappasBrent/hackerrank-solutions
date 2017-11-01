p = int(input())

for _ in range(p):

    a = set(input())
    b = set(input())

    if len(a & b) > 0:
        print('YES')
    else:
        print('NO')
