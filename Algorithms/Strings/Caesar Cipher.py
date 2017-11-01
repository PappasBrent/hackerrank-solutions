import string

input()

s = input()

k = int(input())

res = ''

for letter in s:
    if letter in string.ascii_letters:
        newCharOrd = ord(letter)
        newCharOrd += k
        if letter in string.ascii_lowercase:
            while newCharOrd > 122:
                newCharOrd -= 26
        if letter in string.ascii_uppercase:
            while newCharOrd > 90:
                newCharOrd -= 26

        res += chr(newCharOrd)
    else:
        res += letter

print(res)
