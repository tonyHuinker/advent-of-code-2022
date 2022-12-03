input = open('input.txt')

score = 0
for line in input:
    them = line[0]
    me = line[2]
    if(me == 'X'):
        score = score + 1
        if(them == 'A'):
            score = score + 3
        if (them == 'B'):
            score = score + 0
        if (them == 'C'):
            score = score + 6
    elif(me == 'Y'):
        score = score + 2
        if(them == 'A'):
            score = score + 6
        if (them == 'B'):
            score = score + 3
        if (them == 'C'):
            score = score + 0
    elif (me == 'Z'):
        score = score + 3
        if(them == 'A'):
            score = score + 0
        if (them == 'B'):
            score = score + 6
        if (them == 'C'):
            score = score + 3

print(score)
