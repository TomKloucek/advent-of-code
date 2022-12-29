import os

file = open("input.txt","r")

opening = ['{','[','(','<']

hodnoty = []

chyby = 0

def check_syntax(string):
    stack = []
    for pismeno in string:
        if pismeno in opening:
            stack.insert(0,pismeno)
        else:
            if pismeno == '}':
                if stack[0] != '{':
                    return 1197
                else:
                    stack.pop(0)
            if pismeno == ')':
                if stack[0] != '(':
                    return 3
                else:
                    stack.pop(0)
            if pismeno == ']':
                if stack[0] != '[':
                    return 57
                else:
                    stack.pop(0)
            if pismeno == '>':
                if stack[0] != '<':
                    return 25137
                else:
                    stack.pop(0)
    hodnoty.append(dopln_zavorky_a_spocti(stack))
    return 0

def dopln_zavorky_a_spocti(stack):
    dopln = ''
    for pismeno in stack:
        if pismeno == '{':
            dopln += '}'
        elif pismeno == '(':
            dopln += ")"
        elif pismeno == '[':
            dopln += ']'
        else:
            dopln += '>'
    soucet = 0
    for pismeno in dopln:
        soucet *= 5
        if pismeno == ')':
            soucet += 1
        if pismeno == ']':
            soucet += 2
        if pismeno == '}':
            soucet += 3
        if pismeno == '>':
            soucet += 4
    return soucet

line = file.readline().strip()          
while line:
    chyby += check_syntax(line)
    line = file.readline().strip()

hodnoty = sorted(hodnoty)

print(hodnoty[len(hodnoty)//2])

print(chyby)
