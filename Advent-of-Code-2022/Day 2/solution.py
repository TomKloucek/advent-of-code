import os
file1 = open('input.txt', 'r')

accum = 0
accum_2 = 0

while True:
    line = file1.readline().strip()
    if not line:
        break 
    else:
        vals = line.split(' ')
        print(vals)
        # stage 1
        if vals[0] == 'A':
            if vals[1] == 'X':
                accum += 4
            elif vals[1] == 'Y':
                accum += 8
            else:
                accum += 3
        elif vals[0] == 'B':
            if vals[1] == 'X':
                accum += 1
            elif vals[1] == 'Y':
                accum += 5
            else:
                accum += 9           
        else:
            if vals[1] == 'X':
                accum += 7
            elif vals[1] == 'Y':
                accum += 2
            else:
                accum += 6
        # stage 2
        if vals[1] == 'X':
            if vals[0] == 'A':
                accum_2 += 3
            elif vals[0] == 'B':
                accum_2 += 1
            else:
                accum_2 += 2
        elif vals[1] == 'Y':
            if vals[0] == 'A':
                accum_2 += 4
            elif vals[0] == 'B':
                accum_2 += 5
            else:
                accum_2 += 6
        else:
            if vals[0] == 'A':
                accum_2 += 8
            elif vals[0] == 'B':
                accum_2 += 9
            else:
                accum_2 += 7
print(accum, accum_2)