import string

t=int(input())

s=input()

for letter in string.ascii_lowercase:
    if s.count(letter) == 1:
        s = s.replace(letter, "")
    if str(letter+letter) in s:
        s=s.replace(letter, '')

print(s)

print(len(s))
