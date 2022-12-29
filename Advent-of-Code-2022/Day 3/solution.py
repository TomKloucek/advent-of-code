import os
file1 = open('input.txt', 'r')

counter = 0
accum = 0
second_accum = 0

team_counter = 0

team = []

priorities = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
while True:
    if counter == 3:
        for i in team[0]:
            if i in team[1]:
                if i in team[2]:
                    second_accum += (priorities.index(i)+1)
                    break
        counter = 0
        team_counter += 1
        team = []
    counter += 1

    line = list(file1.readline().strip())
    team.append(line)
    if not line:
        break 
    part1 = line[0:((len(line))//2)]
    part2 = line[((len(line))//2):]
    for i in part1:
        if i in part2:
            accum += (priorities.index(i)+1)
            break
for i in team[0]:
    if i in team[1]:
        if i in team[2]:
            second_accum += (priorities.index(i)+1)
            break

print(accum, second_accum, team_counter)
