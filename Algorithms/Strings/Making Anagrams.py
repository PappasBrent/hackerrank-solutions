import string

a = input()
b = input()

count = 0
for char in string.ascii_lowercase:
    count += abs(a.count(char) - b.count(char))

print(count)