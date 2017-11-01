import string

heights = list(map(int,input().split()))

heightsDict = {}

for letter in string.ascii_lowercase:
    heightsDict[letter] = heights[string.ascii_lowercase.index(letter)]

s = input()

print(heightsDict[max(s, key=lambda c: heightsDict[c])] * len(s))
