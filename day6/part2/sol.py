inf = open("input.txt")

line = inf.readlines()
#line = ["mjqjpqmgbljsphdztnvjfqwrcgsmlb", "sdkjf"]

for x in range(len(line[0])):
    sset = set(line[0][x:x+14])
    if(len(sset) > 13):
        print(x)
        print(x+14)
        print(line[0][x:x+14])
        print(sset)
        input("win!")
