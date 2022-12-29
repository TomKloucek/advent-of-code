
line = file1.readline().strip()
length = len(line)
numbers_of_ones = [0 for x in range(length)]
for cislo in range(0,length):
        if line[cislo] == '1':
            numbers_of_ones[cislo] += 1

while True:
    if not line:
        break
    line = file1.readline().strip()
    length = len(line)
    count_of_lines += 1
    for cislo in range(0,length):
        if line[cislo] == '1':
            numbers_of_ones[cislo] += 1
    array_for_filtering.append(line)

gamma = ''
epsilon = ''

for x in numbers_of_ones:
    if int(x) >= count_of_lines//2:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

array_for_filtering = array_for_filtering[:-1]

oxygen_arr = array_for_filtering.copy()
scrubber_arr = array_for_filtering.copy()

length = len(gamma)

# count oxygen
index = 0
oxygen_len = len(oxygen_arr)
while oxygen_len > 1:
    new_oxygen_arr = []

    numbers_of_ones = [0 for x in range(length)]
    numbers_of_zeros = [0 for x in range(length)]

    for line in oxygen_arr:
        for cislo in range(0,length):
            if line[cislo] == '1':
                numbers_of_ones[cislo] += 1
            else:
                numbers_of_zeros[cislo] += 1

    gamma_ = ''
    for x in range(length):
        if  numbers_of_ones[x] >= numbers_of_zeros[x]:
            gamma_ += '1'
        else:
            gamma_ += '0'
    
    for number in oxygen_arr:
        if number[index] == gamma_[index]:
            new_oxygen_arr.append(number)
    index += 1
    oxygen_arr = new_oxygen_arr
    oxygen_len = len(oxygen_arr)

# count scrubber
index = 0
while len(scrubber_arr) > 1:
    numbers_of_ones = [0 for x in range(length)]
    numbers_of_zeros = [0 for x in range(length)]

    for line in scrubber_arr:
        for cislo in range(0,length):
            if line[cislo] == '1':
                numbers_of_ones[cislo] += 1
            else:
                numbers_of_zeros[cislo] += 1
    char = ''
    if numbers_of_zeros[index] <= numbers_of_ones[index]:
        char = '0'
    else:
        char += '1'
    
    scrubber_arr = [x for x in scrubber_arr if x[index] == char]
    index += 1

gamma = int(gamma,2)
epsilon = int(epsilon,2)

print("first:"+str(gamma*epsilon))

print(int(oxygen_arr[0],2))
print(int(scrubber_arr[0],2))


print("second:"+str(int(oxygen_arr[0],2)*int(scrubber_arr[0],2)))

file1.close()
