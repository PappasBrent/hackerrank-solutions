import string

t = int(input())

for i in range(t):
    s = input()
    if len(s) % 2 != 0:
        print(-1)
        continue

    firstWord = s[:int(len(s) / 2)]
    secondWord = s[int(len(s) / 2):]

    count = 0

    for char in string.ascii_lowercase:
        count += abs(firstWord.count(char) - secondWord.count(char))

    count = int(count/2)
    # print(firstWord, secondWord)
    print(count)
