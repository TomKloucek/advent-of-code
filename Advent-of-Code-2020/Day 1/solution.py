from itertools import combinations
from math import prod
import sys
import os

numbs = []
with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    numbs = [int(line.rstrip()) for line in f]

cmbs2 = list(combinations(numbs,2))
cmbs3 = list(combinations(numbs,3))

sol = []
for el in cmbs2:
    if sum(el) == 2020:
        sol.append(el)
for el in cmbs3:
    if sum(el) == 2020:
        sol.append(el)

print(f'Reseni pro 2 prvky: {prod(sol[0])}')
print(f'Reseni pro 3 prvky: {prod(sol[1])}')
