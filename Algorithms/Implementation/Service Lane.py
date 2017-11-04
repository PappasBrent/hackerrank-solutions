n, t = map(int, input().split())

w = list(map(int, input().split()))

for _ in range(t):
    i, j = map(int,input().split())
    biggestVehicle = 3
    for k in range(i,j+1):
        if w[k] < biggestVehicle:
            biggestVehicle = w[k]
    
    print(biggestVehicle)