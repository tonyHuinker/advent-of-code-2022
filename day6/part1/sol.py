inf = open("input.txt")

line = inf.readlines()
#line = ["mjqjpqmgbljsphdztnvjfqwrcgsmlb", "sdkjf"]

for x in range(len(line[0])):
    sset = set(line[0][x:x+4])
    if(len(sset) > 3):
        print(x)
        print(x+4)
        print(line[0][x:x+4])
        print(sset)
        input("win!")
