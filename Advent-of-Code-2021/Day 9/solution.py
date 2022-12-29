import os

file1 = open("input.txt",'r')

board = []
mins = []
mins_positions = []

line = [int(x) for x in list(file1.readline().strip())]

while line != []:
    board.append(line)
    line = [int(x) for x in list(file1.readline().strip())]

def count_min_adjascents(board):
    soucet = 0
    for y in range(len(board)):
        for x in range(len(board[0])):
            # rohy
            if (x == 0 and y == 0 and  board[y][x] < board[y+1][x] and board[y][x] < board[y][x+1]) or (x == 0 and y == (len(board)-1) and board[y][x] < board[y-1][x] and board[y][x] < board[y][x+1]) or (x == (len(board[0])-1) and y == 0 and board[y][x] < board[y][x-1] and board[y][x] < board[y+1][x]) or (x == (len(board[0])-1) and y == (len(board)-1) and board[y][x] < board[y][x-1] and board[y][x] < board[y-1][x]):
                mins.append(board[y][x]+1)
                mins_positions.append([x,y])
            # leva rada
            elif (x == 0 and board[y][x] < board[y][x+1] and board[y][x] < board[y+1][x] and board[y][x] < board[y-1][x]):
                mins.append(board[y][x]+1)
                mins_positions.append([x,y])
            # prava rada
            elif (x == (len(board[0])-1) and board[y][x] < board[y][x-1] and board[y][x] < board[y+1][x] and board[y][x] < board[y-1][x]):
                mins.append(board[y][x]+1)
                mins_positions.append([x,y])
            # horni rada
            elif (y == 0 and board[y][x] < board[y][x-1] and board[y][x] < board[y][x+1] and board[y][x] < board[y+1][x]):
                mins.append(board[y][x]+1)
                mins_positions.append([x,y])
            # dolni rada
            elif (y == (len(board)-1) and board[y][x] < board[y][x-1] and board[y][x] < board[y][x+1] and board[y][x] < board[y-1][x]):
                mins.append(board[y][x]+1)
                mins_positions.append([x,y])
            elif ((y != 0 and x != 0 and x != (len(board[0])-1) and y != (len(board)-1)) and board[y][x] < board[y-1][x] and board[y][x] < board[y+1][x] and board[y][x] < board[y][x-1] and board[y][x] < board[y][x+1]):
                mins.append(board[y][x]+1)
                mins_positions.append([x,y])
    print(soucet)

def count_basins(list_of_positions:list):
    basins = []
    for position in list_of_positions:
        basins.append(count_basin(position[0],position[1],0,[]))
    return basins

def count_basin(x,y,soucet,visited):
    visited.append([x,y])
    # leva
    if (x-1 >= 0):
        if (board[y][x-1] != 9 and board[y][x-1] > board[y][x] and [x-1,y] not in visited):
            soucet += count_basin(x-1,y,soucet,visited)
    # prava
    if (x+1 <= len(board[0])-1):
        if (board[y][x+1] != 9 and board[y][x+1] > board[y][x] and [x+1,y] not in visited):
            soucet += count_basin(x+1,y,soucet,visited)
    # horni
    if (y-1 >= 0):
        if (board[y-1][x] != 9 and board[y-1][x] > board[y][x] and [x,y-1] not in visited):
            soucet += count_basin(x,y-1,soucet,visited)
    # dolni
    if (y+1 <= len(board)-1):
        if (board[y+1][x] != 9 and board[y+1][x] > board[y][x] and [x,y+1] not in visited):
            soucet += count_basin(x,y+1,soucet,visited)
    return len(visited)

count_min_adjascents(board)
print(sum(mins))

basins = count_basins(mins_positions)
print(basins)

soucin = 1
for i in range(3):
    maximalni = max(basins)
    soucin *= maximalni
    basins.remove(maximalni)

print(soucin)

# 2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678