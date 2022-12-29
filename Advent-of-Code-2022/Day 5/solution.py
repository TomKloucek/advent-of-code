#    [H]         [D]     [P]        
#[W] [B]         [C] [Z] [D]        
#[T] [J]     [T] [J] [D] [J]        
#[H] [Z]     [H] [H] [W] [S]     [M]
#[P] [F] [R] [P] [Z] [F] [W]     [F]
#[J] [V] [T] [N] [F] [G] [Z] [S] [S]
#[C] [R] [P] [S] [V] [M] [V] [D] [Z]
#[F] [G] [H] [Z] [N] [P] [M] [N] [D]
# 1   2   3   4   5   6   7   8   9 

import os
file1 = open('input.txt', 'r')

boxes = [['W','T','H','P','J','C','F'],
         ['H','B','J','Z','F','V','R','G'],
         ['R','T','P','H'],
         ['T','H','P','N','S','Z'],
         ['D','C','J','H','Z','F','V','N'],
         ['Z','D','W','F','G','M','P'],
         ['P','D','J','S','W','Z','V','M'],
         ['S','D','N'],
         ['M','F','S','Z','D']]
while True:
    line = file1.readline().strip()
    if not line:
        break 
    val = line.split(' ')
    #for i in range(int(val[1])):
    #    box = boxes[int(val[3])-1].pop(0)
    #    boxes[int(val[5])-1].insert(0, box)
    to_be_moved = []
    for i in range(int(val[1])):
        box = boxes[int(val[3])-1].pop(0)
        to_be_moved.append(box)
    for i in reversed(to_be_moved):
        boxes[int(val[5])-1].insert(0, i)


for i in boxes:
    print(i[0], end='')
    