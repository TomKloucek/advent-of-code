import os
from collections import deque

file1 = open("input.txt", "r")

pocatecni_ryby = [int(x) for x in file1.readline().strip().split(",")]

ryby = deque()
[ryby.append(0) for _ in range(9)]

for x in pocatecni_ryby:
    ryby[x] += 1

def evoluce(pocet_evoluci):
    for i in range(pocet_evoluci):
        ryby.rotate(-1)
        ryby[6] += ryby[8]
        #print(ryby)

# def evoluce(pocet_evoluci):
#     for j in range(1, pocet_evoluci + 1):
#         for i in range(len(pocatecni_ryby)):
#             if pocatecni_ryby[i] == 0:
#                 pocatecni_ryby[i] = 6
#                 pocatecni_ryby.append(8)
#             else:
#                 pocatecni_ryby[i] -= 1
#         # print(f'Den {j} - {pocatecni_ryby}')

print(ryby)
evoluce(256)
print(sum(ryby))
