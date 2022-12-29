
import os
file1 = open('input.txt', 'r')

line = list(file1.readline().strip())

numbers = [line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8],line[9],line[10],line[11],line[12],line[13]]

line = line[14:]
counter = 14


for i in line:
    okej = True
    for j in numbers:
        if (numbers.count(j) > 1):
            okej = False
    if okej:
        print(counter)
        break
    counter += 1
    numbers.pop(0)
    numbers.append(i)
    