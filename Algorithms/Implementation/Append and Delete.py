s1 = input()
s2 = input()
k = int(input())

# Index at which the two strings differ
i = 0

while i < min([len(s1), len(s2)]) and s1[i] == s2[i]:
    i += 1

print(i)

numOperationsNeeded = len(s1) + len(s2) - 2 * i

if numOperationsNeeded > k:
    print('No')
elif numOperationsNeeded % 2 == k % 2:
    print('Yes')
elif len(s1) + len(s2) - k < 0:
    print('Yes')
else:
    print('No')
