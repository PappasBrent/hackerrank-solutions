t = int(input())

for i in range(t):
    
    count = 0

    n = int(input())

    for digit in str(n):
        if int(digit) != 0 and n % int(digit) == 0:
            count+=1

    print(count)