import os
     
def count_and_decode(list):
    rozdel = list.split(' | ')
    pro_vypocet = rozdel[1].split(' ')
    list = rozdel[0].split(' ')
    cisla = [0 for x in range(0,10)]
    moznosti_na_devet = []
    moznosti_na_trojku = []
    hodnoty = [0 for x in range(7)]
    for x in list:
        if len(x) == 2:
            cisla[1] = x
        if len(x) == 3:
            cisla[7] = x
        if len(x) == 4:
            cisla[4] = x
        if len(x) == 7:
            cisla[8] = x
        if len(x) == 6:
            moznosti_na_devet.append(x)
        if len(x) == 5:
            moznosti_na_trojku.append(x)
    horni = []
    horni[:0] = cisla[7]
    horni.remove(cisla[1][0])
    horni.remove(cisla[1][1])
    hodnoty[0] = horni[0]
    cisla[9] = zjisti_devet(moznosti_na_devet,cisla)
    hodnoty = zjisti_dolni(hodnoty,cisla)
    hodnoty = zjisti_levy_dolni(hodnoty,cisla)
    ld = zjisti_pravy_dolni_levy_horni(list)
    hodnoty[5] = ld[0]
    hodnoty[1] = ld[1]
    ld = zjisti_pravy_horni_a_prostredni(list,hodnoty)
    hodnoty[3] = ld[1]
    hodnoty[2] = ld[0]
    #### V tento moment vim kde co je
    cisla = dopln_zbyla_cisla(list,hodnoty,cisla)
    return vypocitej(pro_vypocet, cisla)

def zjisti_devet(list,cisla):
    for x in cisla[4]:
        for kandidat in list:
            if x not in kandidat:
                list.remove(kandidat)
    return list[0]

def zjisti_dolni(hodnoty,cisla):
    horni = []
    horni[:0] = cisla[9]
    for x in cisla[4]:
        horni.remove(x)
    horni.remove(hodnoty[0])
    hodnoty[6] = horni[0]
    return hodnoty

def zjisti_levy_dolni(hodnoty,cisla):
    horni = []
    horni[:0] = cisla[8]
    for x in cisla[9]:
        horni.remove(x)
    hodnoty[4] = horni[0]
    return hodnoty

def zjisti_pravy_dolni_levy_horni(list):
    pismena = ['a','b','c','d','e','f','g']
    hodnoty = [0 for x in range(7)]
    for x in list:
        if 'a' in x:
            hodnoty[0] += 1
        if 'b' in x:
            hodnoty[1] += 1
        if 'c' in x:
            hodnoty[2] += 1
        if 'd' in x:
            hodnoty[3] += 1
        if 'e' in x:
            hodnoty[4] += 1
        if 'f' in x:
            hodnoty[5] += 1
        if 'g' in x:
            hodnoty[6] += 1
    pravy_dolni = hodnoty.index(max(hodnoty))
    jedna = pismena.pop(pravy_dolni)
    hodnoty.pop(pravy_dolni)
    levy_horni = hodnoty.index(6)
    dva = pismena.pop(levy_horni)
    return [jedna,dva]

def zjisti_pravy_horni_a_prostredni(list,hodnoty_cisel):
    pismena = ['a','b','c','d','e','f','g']
    hodnoty = [0 for x in range(7)]
    for x in list:
        if 'a' in x:
            hodnoty[0] += 1
        if 'b' in x:
            hodnoty[1] += 1
        if 'c' in x:
            hodnoty[2] += 1
        if 'd' in x:
            hodnoty[3] += 1
        if 'e' in x:
            hodnoty[4] += 1
        if 'f' in x:
            hodnoty[5] += 1
        if 'g' in x:
            hodnoty[6] += 1
    pravy = ''
    prostredni = ''
    for i in range(7):
        if hodnoty[i] == 8 and pismena[i] not in hodnoty_cisel:
            pravy = pismena[i]
        if hodnoty[i] == 7 and pismena[i] not in hodnoty_cisel:
            prostredni = pismena[i]
    return [pravy,prostredni]

def dopln_zbyla_cisla(list,hodnoty,cisla):
    for cislo in list:
        if hodnoty[0] in cislo and hodnoty[1] in cislo and hodnoty[2] in cislo and hodnoty[3] not in cislo and hodnoty[4] in cislo and hodnoty[5] in cislo and hodnoty[6] in cislo:
            cisla[0] = cislo
        if hodnoty[0] in cislo and hodnoty[1] not in cislo and hodnoty[2] in cislo and hodnoty[3] in cislo and hodnoty[4] in cislo and hodnoty[5] not in cislo and hodnoty[6] in cislo:
            cisla[2] = cislo
        if hodnoty[0] in cislo and hodnoty[1] not in cislo and hodnoty[2] in cislo and hodnoty[3] in cislo and hodnoty[4] not in cislo and hodnoty[5] in cislo and hodnoty[6] in cislo:
            cisla[3] = cislo
        if hodnoty[0] in cislo and hodnoty[1] in cislo and hodnoty[2] not in cislo and hodnoty[3] in cislo and hodnoty[4] not in cislo and hodnoty[5] in cislo and hodnoty[6] in cislo:
            cisla[5] = cislo
        if hodnoty[0] in cislo and hodnoty[1] in cislo and hodnoty[2] not in cislo and hodnoty[3] in cislo and hodnoty[4] in cislo and hodnoty[5] in cislo and hodnoty[6] in cislo:
            cisla[6] = cislo
    return cisla

def vypocitej(list, cisla):
    soucet = ''
    cisla = [''.join(sorted(x)) for x in cisla]
    list = [''.join(sorted(x)) for x in list]
    print(cisla)
    for x in list:
        soucet += str(cisla.index(x))
    return int(soucet)

###      ______ horni 0
# levy 1 |    | pravy 2
#        ------ prostredni 3
# levy 4 |    | pravy 5
#        ______ dolni 6 

file1 = open("input.txt","r")

line = file1.readline().strip()
soucet = 0
line_count = 0

while line != '':
    soucet += count_and_decode(line)
    line_count += 1
    line = file1.readline().strip()

print(soucet)
