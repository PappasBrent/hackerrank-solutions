import string

for _ in range(int(input())):
    n = int(input())
    b = input()

    if '_' in b:
        board = list(b.replace('_', ''))
        board.sort()
        b = ''.join(board)
        # print(''.join(board))

    unhappy = False
    for letter in filter(lambda c: c in b, string.ascii_uppercase):
        if (letter + letter) not in b:
            # print('Couldn\'t find', letter+letter)
            unhappy = True
            break

    if unhappy:
        print('NO')
        continue

    print('YES')
