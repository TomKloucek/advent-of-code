import os
file1 = open('input.txt', 'r')

pole = []
current = 0

count = 0

line = file1.readline().strip()
pole.append(int(line))

while True:
    line = file1.readline().strip()
    if not line:
        break 
    if len(pole) < 3:
        pole.append(int(line))
    else:
        pole.pop(0)
        pole.append(int(line))

    if sum(pole) > current and len(pole) == 3:
        count += 1
    if len(pole) == 3:
        current = sum(pole)
    
print(count-1)
file1.close()