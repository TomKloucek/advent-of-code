file = open('input.txt').readlines()
rows = []
for line in file:
    line = line.rstrip('\n')
    rows.append([i for i in line])

def pocet_stromu(right,down,rows):
    trees = 0
    x, y = 0, 0
    while y < len(rows):
        if x + right > len(rows[y]) - 1:
            y += down
            x -= (len(rows[y])-right)
        else:
            x += right
            y += down
        if y == len(rows)-1:
            if rows[y][x] == '#':
                trees += 1
            break
        if rows[y][x] == '#':
            trees += 1
    return trees

print(f'Potkanych stromu: {pocet_stromu(1,2,rows)}')

