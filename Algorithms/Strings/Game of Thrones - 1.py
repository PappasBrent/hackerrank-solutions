import string

s = input()

# Number of letters whose count is odd
numOddLettersCount = 0

# Checks the count of each letter in the alphabet in the input string s
for char in string.ascii_lowercase:
    if s.count(char) % 2 != 0:
        numOddLettersCount += 1

# print(numOddLettersCount)
# If there exists more than one letter in the string whose count is odd,
# then there is logically no way to evenly split the string up into equal halves
# which are identical.
# If there is just one letter whose count is odd, then a palindrome can still be
# made by placing that letter in the center of the anagram
if numOddLettersCount > 1:
    print('NO')
else:
    print('YES')