import os
import sys
import re


def split_input():
    with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
        lines = f.read()
        tests = lines.split("\n\n")
        return tests


def parse_test(pole_input, otazka:int):
    fields = []
    for i in pole_input:
        i = i.replace('\n', ' ').split()
        field = []
        for value in i:
            value = value.split(':')
            if otazka == 2:
                if value[0] == 'byr' and (1920 <= int(value[1]) <= 2002):
                    field.append(value[0])
                if value[0] == 'iyr' and (2010 <= int(value[1]) <= 2020):
                    field.append(value[0])
                if value[0] == 'eyr' and (2020 <= int(value[1]) <= 2030):
                    field.append(value[0])
                if value[0] == 'hgt' and (value[1][::-1][0:2] == 'mc' or value[1][::-1][0:2] == 'ni'):
                    if value[1][::-1][0:2] == 'mc' and 150 <= int(value[1][::-1][2:][::-1]) <= 193:
                        field.append(value[0])
                    elif value[1][::-1][0:2] == 'ni' and 59 <= int(value[1][::-1][2:][::-1]) <= 76:
                        field.append(value[0])
                if value[0] == 'hcl' and re.match("^#[a-fA-F0-9]{6}$", value[1]):
                    field.append(value[0])
                if value[0] == 'ecl' and value[1] in ['amb', 'blu', 'grn', 'gry', 'brn', 'hzl', 'oth']:
                    field.append(value[0])
                if value[0] == 'pid' and re.match('[0-9]{9}', value[1]):
                    field.append(value[0])
            else:
                field.append(value[0])
        fields.append(field)
    return fields


def valid_passports(fields):
    valid = 0
    for field in fields:
        if len(field) >= 7:
            if len(field) == 8:
                valid += 1
            if 'cid' not in field and len(field) == 7:
                valid += 1
    return valid


if __name__ == "__main__":
    pole = split_input()
    print(f'Prvni otazka: {valid_passports(parse_test(pole, 1))}')
    print(f'Druha otazka: {valid_passports(parse_test(pole, 2))-1}')

