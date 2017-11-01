n = int(input())

for i in range(n):
    x, y, z = map(int, input().split())

    if abs(z - x) == abs(y - z):
        print("Mouse C")
    else:
        if abs(x - z) < abs(z - y):
            print("Cat A")
        else:
            print("Cat B")
