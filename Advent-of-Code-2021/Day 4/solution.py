import os

boards = [] 
poradi = ''

def change(cislo,board):
    if board == 0:
        return board
    for i in range(0,5):
        for j in range(0,5):
            if board[i][j] == cislo:
                board[i][j] = 'x' 
    return board

def move(cislo):
    for i in range(0,len(boards)):
        boards[i] = change(cislo,boards[i])

def check_win(board):
    win = False
    # checkni sloupce
    for i in range(0,5):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and  board[i][2] == board[i][3] and board[i][3] == board[i][4]:
            win = True

    # checkni radky
    for i in range(0,5):
        if board[0][i] == board[1][i] and  board[1][i] == board[2][i] and board[2][i] == board[3][i] and board[3][i] == board[4][i]:
            win = True

    return win

def hra():
    konec = False
    vitez = 0
    for cislo in poradi:
        move(cislo)
        for i in range(0,len(boards)):
            vysledek = check_win(boards[i])
            if vysledek:
                vitez = i
                konec = True
                break
        if konec:
            break
    vysledek = vypocet(cislo,vitez)
    return vysledek

def hra_second():
    pocet_nul = 0
    for cislo in poradi:
        if pocet_nul == len(boards)-1:
            break
        move(cislo)
        for i in range(0,len(boards)):
            if boards[i] != 0:
                vysledek = check_win(boards[i])
                if vysledek:
                    boards[i] = 0
        pocet_nul = 0
        for board in boards:
            if board == 0:
                pocet_nul += 1
            else:
                print(f'{cislo} - {board}')
        # for board in boards:
        #    print(f'{cislo} - {board}')
        print()
    print(cislo)
    for i in range(0,len(boards)):
        if boards[i] != 0:
            vysledek = vypocet(cislo,i)
    return vysledek

def vypocet(cislo,result):
    soucet = 0
    board = boards[result]
    print(board)
    for radek in board:
        for sloupec in radek:
            if sloupec != 'x' and sloupec != cislo:
                soucet += int(sloupec)
    return soucet*int(cislo)


file1 = open('input.txt', 'r')

poradi = file1.readline().strip().split(',')
file1.readline()
empty = 'x'
while empty != '':
    board = []
    for i in range(0,5):
        line = file1.readline().strip().split()
        if line:
            board.append(line)
        else:
            break
    boards.append(board)
    empty = file1.readline()

print(hra())
print(hra_second())