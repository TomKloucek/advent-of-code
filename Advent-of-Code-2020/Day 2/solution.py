import os
import sys

def nacti_soubor():
    pole = []
    with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
        pole =[line for line in f]
    return pole

def first_policy(pole):
    valid = 0
    for line in pole:
        line = line.split()
        od, do = line[0].split('-')
        znak = line[1][:-1]
        heslo = line[2]
        if int(od) <= heslo.count(znak) <= int(do):
            valid += 1
    return valid

def second_policy(pole):
    valid = 0
    for line in pole:
        line = line.split()
        prvni, druhy = line[0].split('-')
        znak = line[1][:-1]
        heslo = line[2]
        pocet = 0
        if znak == heslo[int(prvni)-1]: pocet += 1
        if znak == heslo[int(druhy)-1]: pocet += 1
        if pocet == 1:
            valid += 1
    return valid

pole = nacti_soubor()

reseni_1 = first_policy(pole)
reseni_2 = second_policy(pole)

print(f'Reseni 1: {reseni_1}')
print(f'Reseni 2: {reseni_2}')