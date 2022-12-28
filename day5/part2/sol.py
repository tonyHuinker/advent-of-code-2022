inf = open('input.txt')

stacks = [[], [], [], [], [], [], [], [], [], []]
stacks[1] = ['L', 'N', 'W', 'T', 'D']
stacks[2] = ['C', 'P','H']
stacks[3] = ['W', 'P', 'H', 'N', 'D', 'G', 'M', 'J']
stacks[4] = ['C', 'W', 'S', 'N', 'T', 'Q', 'L']
stacks[5] = ['P', 'H', 'C', 'N']
stacks[6] = ['T', 'H', 'N', 'D', 'M', 'W', 'Q', 'B']
stacks[7] = ['M', 'B', 'R', 'J', 'G', 'S', 'L']
stacks[8] = ['Z', 'N', 'W', 'G', 'V', 'B', 'R', 'T']
stacks[9] = ['W', 'G', 'D', 'N', 'P', 'L']

for line in inf:
    splitline = line.split(" ")
    if splitline[0] == "move":
        Move = int(splitline[1])
        From = int(splitline[3])
        To = int(splitline[5])
        stacks[To] = stacks[To] + stacks[From][-Move:]
        stacks[From] = stacks[From][:len(stacks[From]) - Move]

for y in range(1, 10):
    print(stacks[y][-1])
