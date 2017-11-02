n = int(input())

a = list(map(int, input().split()))

for i in range(1,len(a)+1):
    x = i
    x = a.index(x)+1
    y = a.index(x)+1
    print(y)