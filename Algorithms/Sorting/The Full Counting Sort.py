n = int(input())

a = [[] for x in range(n)]

for i in range(n):
    k, s = input().split()
    k = int(k)
    if i < n / 2:
        a[k].append('-')
    else:    
        a[k].append(s)

# print(a)

for strings in a:
    print(*strings, end=' ')
