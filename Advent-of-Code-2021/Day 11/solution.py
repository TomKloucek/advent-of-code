file = open("test.txt","r")

board = []
flashes = 0

line = file.readline()
while line:
    line = [int(x) for x in line.strip()]
    board.append(line)
    line = file.readline()

def round():
    flashes = 0
    for y in range(len(board)-1):
        for x in range(len(board[0])-1):
            board[y][x] += 1
            if board[y][x] > 9:
                flashes += 1
                if y==0 and x==0:
                    board[y][x+1] += 1
                    board[y+1][x+1] += 1
                    board[y+1][x] += 1
                elif x==len(board[0])-1 and y==0:
                    board[y][x-1] += 1
                    board[y+1][x-1] += 1
                    board[y+1][x] += 1
                elif x==0 and y==len(board)-1:
                    board[y-1][x+1] += 1
                    board[y-1][x] += 1
                    board[y][x+1] += 1
                elif x==len(board[0])-1 and y==len(board)-1:
                    board[y][x-1] += 1
                    board[y-1][x-1] += 1
                    board[y-1][x] += 1
                elif y == 0:
                    board[y][x-1] += 1
                    board[y][x+1] += 1
                    board[y+1][x] += 1
                    board[y+1][x-1] += 1
                    board[y+1][x+1] += 1
                elif y == len(board)-1:
                    board[y][x-1] += 1
                    board[y][x+1] += 1
                    board[y-1][x] += 1
                    board[y-1][x-1] += 1
                    board[y-1][x+1] += 1
                elif x == 0:
                    board[y-1][x] += 1
                    board[y+1][x] += 1
                    board[y][x+1] += 1
                    board[y-1][x+1] += 1
                    board[y+1][x+1] += 1
                elif x == len(board[0])-1:
                    board[y-1][x] += 1
                    board[y+1][x] += 1
                    board[y][x-1] += 1
                    board[y-1][x-1] += 1
                    board[y+1][x-1] += 1
                else:
                    board[y-1][x-1] += 1
                    board[y-1][x] += 1
                    board[y-1][x+1] += 1
                    board[y][x-1] += 1
                    board[y][x+1] += 1
                    board[y+1][x-1] += 1
                    board[y+1][x] += 1
                    board[y+1][x+1] += 1
                board[y][x] = 0
    return flashes

def vypis():
    for y in range(len(board)):
        for x in range(len(board[0])):
            print(f" {board[y][x]} ",end='')
        print()
    print()

def rounds_runner(number):
    flashes = 0
    for _ in range(number):
        flashes += round()
        vypis()
    return flashes

print(rounds_runner(10))