# I AM THE GREED MASTER!

t = int(input())

for i in range(t):
    b, w = map(int, input().split())
    x, y, z = map(int, input().split())

    if z >= x and z >= y:
        price = (b * x) + (w * y)
    else:
        if min((x, y)) == x:
            if x * (b + w) + (z * w) < (b * x) + (w * y):
                price = x * (b + w)
                price += z * w
            else:
                price = b * x
                price += w * y

        elif min((x, y)) == y:
            if y * (b + w) + (z * b) < (w * y) + (b * x):
                price = y * (b + w)
                price += z * b
            else:
                price = w * y
                price += b * x

    print(price)
