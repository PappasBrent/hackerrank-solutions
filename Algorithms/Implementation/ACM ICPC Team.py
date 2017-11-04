n, m = map(int, input().split())

people = []

mostVersed = 0

for i in range(n):
    people.append(input())

for person in people:
    for person2 in people:
        if int(person, 2) ^ int(person2, 2) > mostVersed:
            mostVersed = int(person, 2) ^ int(person2, 2)

# print(mostVersed)

count = 0

for person in people:
    for person2 in people:
        if int(person, 2) ^ int(person2, 2) == mostVersed:
            count += 1

print(bin(mostVersed).count('1'))
print(count)
