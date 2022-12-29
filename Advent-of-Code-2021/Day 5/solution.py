import os

souradnice_pole = []
ohodnoceni = []

def pridej_hodnoty(pole):
    od = [int(hodnota) for hodnota in pole[0].strip().split(',')]
    do = [int(hodnota) for hodnota in pole[1].strip().split(',')]
    if od[0] == do[0] and od[1] == do[1]:
        souradnice = [od[0],do[0]]
        if souradnice in souradnice_pole:
            index = souradnice_pole.index(souradnice)
            ohodnoceni[index] += 1
        else:
            souradnice_pole.append(souradnice)
            ohodnoceni.append(1)
        return
    if od[0] == do[0]:
        if od[1] < do[1]:
            for i in range(od[1],do[1]+1):
                souradnice = [od[0],i]
                if souradnice in souradnice_pole:
                    index = souradnice_pole.index(souradnice)
                    ohodnoceni[index] += 1
                else:
                    souradnice_pole.append(souradnice)
                    ohodnoceni.append(1)
        elif od[1] > do[1]:
            for i in range(od[1],do[1]-1,-1):
                souradnice = [od[0],i]
                if souradnice in souradnice_pole:
                    index = souradnice_pole.index(souradnice)
                    ohodnoceni[index] += 1
                else:
                    souradnice_pole.append(souradnice)
                    ohodnoceni.append(1)
    elif od[1] == do[1]:
        if od[0] < do[0]:
            for i in range(od[0],do[0]+1):
                souradnice = [i,od[1]]
                if souradnice in souradnice_pole:
                    index = souradnice_pole.index(souradnice)
                    ohodnoceni[index] += 1
                else:
                    souradnice_pole.append(souradnice)
                    ohodnoceni.append(1)
        elif od[0] > do[0]:
            for i in range(od[0],do[0]-1,-1):
                souradnice = [i,od[1]]
                if souradnice in souradnice_pole:
                    index = souradnice_pole.index(souradnice)
                    ohodnoceni[index] += 1
                else:
                    souradnice_pole.append(souradnice)
                    ohodnoceni.append(1)
    elif od[0] < do[0]:
        if od[1] < do[1]:
            for i in range(0,do[0]-od[0]+1):
                souradnice = [od[0]+i,od[1]+i]
                if souradnice in souradnice_pole:
                    index = souradnice_pole.index(souradnice)
                    ohodnoceni[index] += 1
                else:
                    souradnice_pole.append(souradnice)
                    ohodnoceni.append(1)
        if od[1] > do[1]:
            for i in range(0,(do[0]-od[0]+1)):
                souradnice = [od[0]+i,od[1]-i]
                if souradnice in souradnice_pole:
                    index = souradnice_pole.index(souradnice)
                    ohodnoceni[index] += 1
                else:
                    souradnice_pole.append(souradnice)
                    ohodnoceni.append(1)
    elif od[0] > do[0]:
        if od[1] < do[1]:
            for i in range(0,od[0]-do[0]+1):
                souradnice = [od[0]-i,od[1]+i]
                if souradnice in souradnice_pole:
                    index = souradnice_pole.index(souradnice)
                    ohodnoceni[index] += 1
                else:
                    souradnice_pole.append(souradnice)
                    ohodnoceni.append(1)
        if od[1] > do[1]:
            for i in range(0,od[0]-do[0]+1):
                souradnice = [od[0]-i,od[1]-i]
                if souradnice in souradnice_pole:
                    index = souradnice_pole.index(souradnice)
                    ohodnoceni[index] += 1
                else:
                    souradnice_pole.append(souradnice)
                    ohodnoceni.append(1)

file1 = open("input.txt","r")
values = "neco"
line = 1
while True:
    values = file1.readline().strip().split(" -> ")
    if values == ['']:
        break
    pridej_hodnoty(values)
    #print(f"{line} - {values[0]} = {values[1]}")
    line += 1

print(len(ohodnoceni),len(souradnice_pole))

counter = 0
for x in ohodnoceni:
    if x > 1:
        counter += 1

print(counter)


