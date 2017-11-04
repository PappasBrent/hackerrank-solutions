n = int(input())

s = input()

numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"

hasNum = 0
for char in numbers:
    if char in s:
        hasNum+=1
        break

hasLower = 0
for char in lower_case:
    if char in s:
        hasLower += 1
        break

hasUpper = 0
for char in upper_case:
    if char in s:
        hasUpper += 1
        break

hasSpecial = 0
for char in special_characters:
    if char in s:
        hasSpecial += 1
        break

lengthNeeded = 6
numNeeded = 4 - hasNum - hasLower - hasUpper - hasSpecial

if len(s) < lengthNeeded:
    print(max([lengthNeeded-len(s), numNeeded]))
else:
    print(numNeeded)