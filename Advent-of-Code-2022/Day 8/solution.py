import os
file1 = open('input.txt', 'r')

line = list(file1.readline().strip())

map = []

map.append(line)

accum = 0

while True:
    line = file1.readline().strip()
    if not line:
        break 
    map.append(list(line))

print(map)

scenic_max = 0

x = 0
y = 0
for line in map:
    for tree in line:
        visible = False
        scenic_a = 0
        scenic_b = 0
        scenic_c = 0
        scenic_d = 0

        if x == 0 or x == len(map)-1 or y == 0 or y == len(map[0])-1:
            accum += 1
        else:
            for i in reversed(line[:(x)]):
                if i < tree:
                    scenic_a += 1
                    visible = True
                else:
                    scenic_a += 1
                    visible = False
                    break
            for i in line[(x+1):]:
                if i < tree:
                    scenic_b += 1
                    visible = True
                else:
                    scenic_b += 1
                    visible = False
                    break
            counter = y-1
            while counter >= 0:
                if map[counter][x] < tree:
                    scenic_c += 1
                    visible = True
                else:
                    scenic_c += 1
                    visible = False
                    break
                counter -= 1
            counter = y+1
            while counter < len(map):
                if map[counter][x] < tree:
                    scenic_d += 1
                    visible = True
                else:
                    scenic_d += 1
                    visible = False
                    break
                counter += 1
            print(tree,x,y,scenic_a,scenic_b,scenic_c,scenic_d)
            scenic = scenic_a*scenic_b*scenic_c*scenic_d
            if scenic > scenic_max:
                scenic_max = scenic
        x += 1
    y += 1
    x = 0
print(accum)
print(scenic_max)
