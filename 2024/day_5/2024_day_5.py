part1 = []
part2 = []

switch = False
inputFile = open("2024/day_5/input.txt", "r")
for line in inputFile:
    line = line.strip()
    if not line:
        switch = True
    elif not switch:
        breaking = line.split("|")
        part1.append(breaking)
    else:
        breaking = line.split(",")
        part2.append(breaking)
inputFile.close()

lines_worked = []
for i in part2:
    for x in range(len(i)):
        for y in range(x + 1, len(i)):
            listed = [i[x], i[y]]
            if listed in part1:
                if listed not in lines_worked:
                    lines_worked.append(i)

# print(lines_worked)
sum = 0
find_lines = []
for i in part2:
    bar = 0
    for j in range(len(i)):
        bar += j
    if(lines_worked.count(i) == bar):
        sum += int(i[int(len(i) / 2)])
        find_lines.append(i)
print(sum)

for i in find_lines:
    if i in part2:
        part2.remove(i)
    
lines_worked = []
for i in part2:
    for x in range(len(i)):
        for y in range(x + 1, len(i)):
            listed = [i[x], i[y]]
            listed2 = [i[y], i[x]]
            if listed in part1:
                if listed not in lines_worked:
                    lines_worked.append(i)
            elif listed2 in part1:
                if listed2 not in lines_worked:
                    temp = i[y]
                    i[y] = i[x]
                    i[x] = temp
                    lines_worked.append(i)

sum = 0
find_lines = []
for i in part2:
    bar = 0
    for j in range(len(i)):
        bar += j
    if(lines_worked.count(i) == bar):
        sum += int(i[int(len(i) / 2)])
        find_lines.append(i)
print(sum)