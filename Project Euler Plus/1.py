
# Source; greatly informative and helpful
# https://projecteuler.net/thread=1;post=105728


def sum3and5(N):
    num3Multiples = (N - 1) // 3
    num5Multiples = (N - 1) // 5
    num15Multiples = (N - 1) // 15
    sum3Multiples = 3 * num3Multiples
    sum5Multiples = 5 * num5Multiples
    sum15Multiples = 15 * num15Multiples
    # Note that bitwise right shifts are used instead of simply dividing by 2, as this would create a rounding error
    return (sum3Multiples * (num3Multiples + 1) >> 1) + (sum5Multiples * (num5Multiples + 1) >> 1) - (sum15Multiples * (num15Multiples + 1) >> 1)


c = int(input())

for i in range(c):

    n = int(input())

    print(int(sum3and5(n)))
