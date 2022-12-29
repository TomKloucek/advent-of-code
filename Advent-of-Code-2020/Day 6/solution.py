import os
import sys


def split_input():
    with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
        lines = f.read()
        tests = lines.split("\n\n")
        tests = [x.split('\n') for x in tests]
        return tests


def result(pole):
    numbs = []
    for answers in pole:
        ans = set()
        for i in answers:
            for j in i:
                ans.add(j)
        numbs.append(len(ans))
    return sum(numbs)


def result_two(pole):
    true = 0
    for answers in pole:
        if len(answers) == 1:
            true += len(answers[0])
        else:
            imp = set()
            for cast in answers:
                for letter in cast:
                    imp.add(letter)
            for i in imp:
                if all(i in string for string in answers):
                    true += 1
    return true


if __name__ == "__main__":
    pole = split_input()
    print(result(pole))
    pole = split_input()
    print(pole)
    print(result_two(pole))