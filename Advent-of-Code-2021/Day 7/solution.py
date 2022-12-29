import os

file1 = open("input.txt","r")

array_of_numbers = [int(x) for x in file1.readline().strip().split(',')]

min_num = min(array_of_numbers)
max_num = max(array_of_numbers)

results = []

for i in range(min_num,max_num+1):
    soucet = 0
    for cislo in array_of_numbers:
        soucet += sum([x for x in range(0,abs(cislo-i)+1)])
    results.append(soucet)

print(min(results))
