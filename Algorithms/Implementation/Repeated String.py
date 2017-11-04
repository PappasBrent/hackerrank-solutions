s = input()

n = int(input())

numWords = int(n / len(s))

asPerWord = s.count('a')

numas = numWords * asPerWord

if n % len(s) != 0:
    numas += s[: n % len(s)].count('a')

print(numas)
