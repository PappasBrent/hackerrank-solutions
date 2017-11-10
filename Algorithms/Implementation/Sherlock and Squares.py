from math import sqrt, ceil, floor

t = int(input())

for i in range(t):

    a, b = map(int, input().split())

    # Slow

    # count = 0

    # for i in range(a, b + 1):
    #     if sqrt(i) % 1 == 0:
    #         count+=1

    # print(count)

    # Faster
    # Calculates the number of integer between the squares of the
    # starting and ending numbers
    print(int( floor(sqrt(b)) - ceil(sqrt(a)) + 1) )