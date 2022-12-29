import os
file1 = open('input.txt', 'r')

# width = 0
# depth = 0

# # first solution
# while True:
#     line = file1.readline().strip().split()
#     if not line:
#         break 
#     if line[0] == 'up':
#         depth -= int(line[1])
#     if line[0] == 'down':
#         depth += int(line[1])
#     if line[0] == 'forward':
#         width += int(line[1])
# print(width*depth)

# second solution
aim = 0

width = 0
depth = 0

while True:
    line = file1.readline().strip().split()
    if not line:
        break 
    if line[0] == 'up':
        aim -= int(line[1])
    if line[0] == 'down':
        aim += int(line[1])
    if line[0] == 'forward':
        width += int(line[1])
        depth += (int(line[1])*aim)
print(width*depth)

file1.close()
