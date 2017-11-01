y = int(input())

daysPast = 243

if 1700 <= y <= 1917:
    if y % 4 == 0:
        daysPast += 1
else:
    if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
        daysPast += 1

if y == 1918:
    daysPast = 230


dd = 256 - daysPast
mm = 9
yyyy = y

print('{0:02d}.{1:02d}.{2}'.format(dd,mm,yyyy))