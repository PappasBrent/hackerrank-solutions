import string

s = input()

n = int(input())

# Set is used instead of an array because its faster when checking
vals=set()

# alpha = {}

# for letter in string.ascii_lowercase:
#     alpha[letter] = string.ascii_letters.index(letter) + 1

alpha = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13,
         'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}

for letter in string.ascii_lowercase:
    numConsec = 1
    while(s.find(letter*numConsec) != -1):
        vals.add(alpha[letter] * numConsec)
        numConsec+=1

for i in range(n):
    if int(input()) in vals:
        print('Yes')
    else:
        print('No')
