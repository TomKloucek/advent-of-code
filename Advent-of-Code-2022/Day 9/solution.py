import os
file1 = open('custom.txt', 'r')

map = [[0 for x in range(6)] for y in range(5)]
head = [0,0]
tail = [0,0]
map[0][0] = 1

#map = [[0 for x in range(1000)] for y in range(1000)]
#head = [500,500]
#tail = [500,500]
#map[500][500] = 1

accum = 0

while True:
    line = file1.readline().strip().split()
    print(line, head, tail)
    if not line:
        break 
    if line[0] == 'U':
        for i in range(int(line[1])):
            if i == 0:
                head[1] += 1
                if (abs(head[0]-tail[0]) != 1 and abs(head[1]-tail[1]) >= 1) or (abs(head[0]-tail[0]) >= 1 and abs(head[1]-tail[1]) != 1):
                        tail[1] = head[1]
                        tail[0] += 1
                        map[tail[1]][tail[0]] = 1
            else:
                if head[0] == tail[0]:
                    if head[1] == tail[1]:
                        head[1] += 1
                    else:
                        head[1] += 1
                        tail[1] += 1
                        map[tail[1]][tail[0]] = 1
                else:
                    head[1] += 1
                    if (abs(head[0]-tail[0]) != 1 and abs(head[1]-tail[1]) >= 1) or (abs(head[0]-tail[0]) >= 1 and abs(head[1]-tail[1]) != 1):
                        tail[0] = head[0]
                        tail[1] += 1
                        map[tail[1]][tail[0]] = 1
    elif line[0] == 'D':
        for i in range(int(line[1])):
            if i == 0:
                head[1] -= 1
                if (abs(head[0]-tail[0]) != 1 and abs(head[1]-tail[1]) >= 1) or (abs(head[0]-tail[0]) >= 1 and abs(head[1]-tail[1]) != 1):
                        tail[1] = head[1]
                        tail[0] -= 1
                        map[tail[1]][tail[0]] = 1
            else:
                if head[0] == tail[0]:
                    if head[1] == tail[1]:
                        head[1] -= 1
                    else:
                        head[1] -= 1
                        tail[1] -= 1
                        map[tail[1]][tail[0]] = 1
                else:
                    head[1] -= 1
                    if (abs(head[0]-tail[0]) != 1 and abs(head[1]-tail[1]) == 1) or (abs(head[0]-tail[0]) == 1 and abs(head[1]-tail[1]) != 1):
                        tail[0] = head[0]
                        tail[1] -= 1
                        map[tail[1]][tail[0]] = 1
    elif line[0] == 'R':
        for i in range(int(line[1])):
            if i == 0:
                head[0] += 1
                if (abs(head[0]-tail[0]) != 1 and abs(head[1]-tail[1]) >= 1) or (abs(head[0]-tail[0]) >= 1 and abs(head[1]-tail[1]) != 1):
                        tail[1] = head[1]
                        tail[0] += 1
                        map[tail[1]][tail[0]] = 1
            else:
                if head[1] == tail[1]:
                    if head[0] == tail[0]:
                        head[0] += 1
                    else:
                        head[0] += 1
                        tail[0] += 1
                        map[tail[1]][tail[0]] = 1
                else:
                    head[0] += 1
                    if (abs(head[0]-tail[0]) != 1 and abs(head[1]-tail[1]) >= 1) or (abs(head[0]-tail[0]) >= 1 and abs(head[1]-tail[1]) != 1):
                        tail[1] = head[1]
                        tail[0] += 1
                        map[tail[1]][tail[0]] = 1
    else:
        for i in range(int(line[1])):
            if i == 0:
                head[0] -= 1
                if (abs(head[0]-tail[0]) != 1 and abs(head[1]-tail[1]) >= 1) or (abs(head[0]-tail[0]) >= 1 and abs(head[1]-tail[1]) != 1):
                        tail[1] = head[1]
                        tail[0] -= 1
                        map[tail[1]][tail[0]] = 1
            else:
                if head[1] == tail[1]:
                    if head[0] == tail[0]:
                        head[0] -= 1
                    else:
                        head[0] -= 1
                        tail[0] -= 1
                        map[tail[1]][tail[0]] = 1
                else:
                    head[0] -= 1
                    if (abs(head[0]-tail[0]) != 1 and abs(head[1]-tail[1]) >= 1) or (abs(head[0]-tail[0]) >= 1 and abs(head[1]-tail[1]) != 1):
                        tail[1] = head[1]
                        tail[0] -= 1
                        map[tail[1]][tail[0]] = 1
    for i in reversed(map):
        print(i)
    print()

for row in map:
    accum += row.count(1)

print(accum)
