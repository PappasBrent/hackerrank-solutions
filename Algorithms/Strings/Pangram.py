import string

s=input().lower()

numLetters = 0

for letter in string.ascii_lowercase:
    if s.count(letter)>=1:
        numLetters+=1

if numLetters == 26:
    print("pangram")
else:
    print("not pangram")