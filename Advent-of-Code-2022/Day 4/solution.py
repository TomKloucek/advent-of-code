import os
file1 = open('input.txt', 'r')

accum = 0
accum_two = 0

while True:
    line = file1.readline().strip()
    if not line:
        break 
    elves = line.split(',')
    elf_one = [int(x) for x in elves[0].split('-')]
    elf_two = [int(x) for x in elves[1].split('-')]

    if elf_one[0] >= elf_two[0] and elf_one[1] <= elf_two[1]:
        accum += 1
    elif elf_two[0] >= elf_one[0] and elf_two[1] <= elf_one[1]:
        accum += 1

    if elf_one[1] >= elf_two[0] and elf_one[0] <= elf_two[0]:
        print(elf_one, elf_two)
        accum_two += 1
    elif elf_two[1] >= elf_one[0] and elf_two[0] <= elf_one[0]:
        print(elf_one, elf_two)
        accum_two += 1
    
print(accum, accum_two)