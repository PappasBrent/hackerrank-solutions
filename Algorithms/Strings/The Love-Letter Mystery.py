t = int(input())

for i in range(t):
    s = input()

    if s == s[::-1]:
        print('0')
        continue
    else:
        count = 0
        for letter in s:
            print(letter, ord(letter))
            count += (ord(letter) - ord('a'))

    print(count)