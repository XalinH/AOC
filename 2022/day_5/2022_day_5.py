import math

first = True
moves = False

blocks = []
part1 = []
part2 = []
part3 = []

inputFile = open("2022/day_5/input.txt", "r")
for line in inputFile:
    if(line.strip() == ""):
        moves = True
        for i in range(len(blocks)):
            blocks[i].pop()
        for i in blocks:
            i = i.reverse()
    elif not moves:
        if first:
            for i in range(math.floor(len(line) / 4)):
                blocks.append([])
            first = False
            
        broken = []
        for i in range(len(line)):
            broken.append(line[i])
        for i in range(math.floor(len(broken) / 4)):
            if(broken[1 + i * 4] != " "):
                blocks[i].append(broken[1 + i * 4])
    else:
        broken = line.split()
        part1.append(int(broken[1]))
        part2.append(int(broken[3]))
        part3.append(int(broken[5]))
inputFile.close()
        
for i in blocks:
    print(i)
    
for x in range(len(part1)):
    # for y in range(part1[x]):
    #     blocks[part3[x] - 1].append(blocks[part2[x] - 1][-1])
    #     blocks[part2[x] - 1].pop()
    mini = len(blocks[part2[x] - 1]) - part1[x]
    for i in range(mini, len(blocks[part2[x] - 1])):
        blocks[part3[x] - 1].append(blocks[part2[x] - 1][i])
    # blocks[part3[x] - 1].append(blocks[part2[x] - 1][mini:len(blocks[part2[x] - 1])])
    for i in range(part1[x]):
        blocks[part2[x] - 1].pop()
    print(x)


for i in blocks:
    print(i)
    
total = ""
for i in range(len(blocks)):
    total += blocks[i][-1]
print(total)