import os
file1 = open('input.txt', 'r')

pole = []
accum = 0
last = file1.readline().strip()

accum += int(last)

while True:
    line = file1.readline().strip()
    if not line:
        if not last:
            break 
        else:
            pole.append(accum)
            accum = 0
    else:
        accum += int(line)
    last = line

print(max(pole))

second = 0

for i in range(3):
    res = max(pole)
    second += res
    pole.remove(res)

print(second)