t = int(input())

for i in range(t):
    s = input()
    r = s[::-1]
    
    funny = True
    for i in range(1, int(len(s))):
        if abs(ord(s[i]) - ord(s[i - 1])) != abs(ord(r[i]) - ord(r[i - 1])):
            funny = False
            break
    
    if funny:
        print('Funny')
    else:
        print('Not Funny')
