import os
import sys

contained = set()

def split_input():
    with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
        lines = f.read()
        tests = lines.split("\n")
        tests = [x.split('contain') for x in tests]
        return tests

def contains(list):
    for x in list:
        for bag in x[1].split(','):
            bag = bag.strip()[2:]
            if bag[-1] == 's':
                bag = bag[:-1]
            if 's.' in bag:
                bag = bag[:-2]
            if '.' in bag:
                bag = bag[:-1]
            if bag in contained:
                contained.add(x[0].strip()[:-1])
            elif 'shiny gold bag' in bag:
                contained.add(x[0].strip()[:-1])

if __name__ == "__main__":
    pole = split_input()
    pole = pole[:-1]
    last = 1
    while last != len(contained):
        contains(pole)
        last = len(contained)
    print(len(contained))