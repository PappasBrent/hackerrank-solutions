n = int(input())

for i in range(n):

    s=input()

    ans='YES'

    x = s.find('h')

    for letter in 'ackerrank':
        if x==-1:
            ans='NO'
            break
        else:
            x = s.find(letter,x+1)

    print(ans)
    
