inf = open("input.txt")

overlaps = 0
for line in inf:
    ranges = line.split(',')
    range1 = ranges[0].split("-")
    range2 = ranges[1].split("-")
    list1 = range(int(range1[0]), int(range1[1])+1)
    list2 = range(int(range2[0]), int(range2[1])+1)
    if(not set(list1).isdisjoint(set(list2))):
        overlaps = overlaps +1



print(overlaps)


