input = open('input.txt')

max = 0
sum = 0
for line in input:
    if '\n' == line:
        if sum > max:
            max = sum
        sum = 0
    else:
        sum = sum + int(line)

print(max)
