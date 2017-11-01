x1, v1, x2, v2 = map(int, input().split())

if v1==v2 and x1!=x2:
    print("NO")
    exit()

t = (x1 - x2) / (v2 - v1)

# print(t)

# The time needed for their positions to be equal must be an integer and greater than to be real

if int(t) == t and t > 0:
    print("YES")
else:
    print("NO")