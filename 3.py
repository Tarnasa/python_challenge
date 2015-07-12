__author__ = "Tarnasa"

lines = (''.join(open('3.in').readlines())).split('\n')

a = ''

def check_neighbors(lines, x, y, n, check):
    if not (n <= x <= len(lines[x]) - (n + 1) and n <= y <= len(lines) - (n + 1)):
        return 0
    #return check(lines[y + n][x]) + check(lines[y - n][x]) + check(lines[y][x + n]) + check(lines[y][x - n])
    return check(lines[y][x + n]) * 2 + check(lines[y][x - n]) * 2

for y, line in enumerate(lines):
    for x, letter in enumerate(line):
        if letter.islower():
            for i in range(1, 4):
                if check_neighbors(lines, x, y, i, lambda c: c.isupper()) != 4:
                    break
            else:
                if check_neighbors(lines, x, y, 4, lambda c: c.islower()) == 4:
                    print('found: {}'.format(letter))
                    a += letter
                    for i in range(y, y + 1):
                        print(lines[i][x - 3:x + 4])

print(a)

