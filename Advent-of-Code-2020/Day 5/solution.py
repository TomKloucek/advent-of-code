import os
import sys


def split_input():
    with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
        lines = f.read()
        tests = lines.split("\n")
        return tests

def get_row(pole):
    ids = []
    for rada in pole:
        row = [*range(128)]
        column = [*range(8)]
        for letter in rada:
            values = conquer(letter, row, column)
            row,column = values[0], values[1]

        ids.append(row[0]*8+column[0])
    return ids


def conquer(letter,row,column):
    if letter == 'F':
        row = row[:int(len(row)/2)]
    elif letter == 'B':
        row = row[int(len(row)/2):]
    elif letter == 'R':
        column = column[int(len(column)/2):]
    else:
        column = column[:int(len(column)/2)]
    return row, column

def occupied(pole):
    occupied = [*range(89, 990)]
    for seat in occupied:
        if seat not in pole:
            return seat


if __name__ == "__main__":
    pole = split_input()
    print(max(get_row(pole)))
    print(occupied(get_row(pole)))