input = open('input.txt')

score = 0
for line in input:
    them = line[0]
    result = line[2]
    if(them == 'A'):
        if(result == 'X'):
            score = score + 3
        if (result == 'Y'):
            score = score + 4
        if (result == 'Z'):
            score = score + 8
    elif(them == 'B'):
        if (result == 'X'):
            score = score + 1
        if (result == 'Y'):
            score = score + 5
        if (result == 'Z'):
            score = score + 9
    elif(them == 'C'):
        if (result == 'X'):
            score = score + 2
        if (result == 'Y'):
            score = score + 6
        if (result == 'Z'):
            score = score + 7

print(score)
