t = int(input())

for i in range(t):

    numRemoved = 0
    s = input()

    for c in range(len(s) - 1):
        if s[c] == s[c+1]:
            numRemoved+=1
    
    print(numRemoved)