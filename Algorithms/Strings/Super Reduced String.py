import string

s = input()


def checkForDuplicates():
    global s
    c = 0
    while c < len(string.ascii_lowercase):
        if s.count(string.ascii_lowercase[c] * 2) > 0:
            while s.count(string.ascii_lowercase[c] * 2) > 0:
                s = s.replace(string.ascii_lowercase[c] * 2, '')
            c = 0
        c += 1
    for letter in string.ascii_lowercase:
        if s.count(letter * 2) > 0:
            return True
    return False


containsDuplicates = True
while containsDuplicates:
    containsDuplicates = checkForDuplicates()

if len(s) != 0:
    print(s)
else:
    print("Empty String")
