input = open('input.txt')

sum = 0
elves = []
for line in input:
    if '\n' == line:
        elves.append(sum)
        sum = 0
    else:
        sum = sum + int(line)

elves.sort(reverse=True)
sum = elves[0] + elves[1] + elves[2]
print(sum)