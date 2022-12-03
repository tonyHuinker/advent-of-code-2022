inf = open('input.txt')

#38
#96

linenum = 0
lines = []
groups = 0
badges = []
for line in inf:
    linenum = linenum + 1
    lines.append(line.strip())
    if ((linenum % 3) == 0):
        badges.append(set(lines[groups*3 + 0])  & set(lines[groups*3 + 1]) & set(lines[groups*3 + 2]))
        groups = groups + 1

score = 0
print(ord('a'))
print(ord('z'))
print(ord('A'))
print(ord('Z'))
for badge in badges:
    print(badge)
    if(str(badge).isupper()):
        score = score + (ord(badge.pop())-38)
    else:
        score = score + (ord(badge.pop())-96)

print(score)








