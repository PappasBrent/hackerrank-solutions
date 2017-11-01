import string

n = int(input())

gems = set(string.ascii_lowercase)
for i in range(n):
    s = set(input())
    gems = gems & (s)

print(len(gems))