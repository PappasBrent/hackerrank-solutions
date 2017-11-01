n = int(input())

ar = list(map(int, input().split()))

for i in range(1, len(ar)):
    e = ar[i]
    j = i - 1
    while j >= 0 and ar[j] > e:
        ar[j + 1] = ar[j]
        j = j - 1
    ar[j+1] = e
    print(*ar)
        
