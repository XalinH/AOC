# Average time per: 21 minutes
# numbers = []
lines = []
inputFile = open("2025/day_6/input.txt", "r")
for line in inputFile:
    # line = line.strip()
    if(line[0] != "+" and line[0] != "*"):
        # line = line.split()
        # numbers.append(line)
        lines.append(line)
    else:
        equator = line.split()
inputFile.close
# print(equator)

# sum = 0
# for i in range(len(equator)):
#     if(equator[i] == "+"):
#         add = 0
#         for j in range(len(numbers)):
#             add += int(numbers[j][i])
#         sum += add
#     elif(equator[i] == "*"):
#         multiply = int(numbers[0][i])
#         for j in range(1, len(numbers)):
#             multiply *= int(numbers[j][i])
#         sum += multiply

# print(sum)
sum = 0
for i in range(len(equator)):
    splited = []
    print(len(lines[0]))
    for x in range(len(lines[0])):
        if(len(lines[0]) == 4):
            splited.append(lines[0][:3])
            splited.append(lines[1][:3])
            splited.append(lines[2][:3])
            splited.append(lines[3][:3])
            break
        elif((lines[0][x] == " " and lines[1][x] == " " and lines[2][x] == " " and lines[3][x] == " ")):
            splited.append(lines[0][:x])
            splited.append(lines[1][:x])
            splited.append(lines[2][:x])
            splited.append(lines[3][:x])
            lines[0] = lines[0][x + 1:]
            lines[1] = lines[1][x + 1:]
            lines[2] = lines[2][x + 1:]
            lines[3] = lines[3][x + 1:]
            break
    rotated = [""] * len(splited[0])
    for j in range(len(splited)):
        for k in range(len(splited[j])):
            rotated[k] += splited[j][k]
    
    print(rotated)
    if(equator[i] == "+"):
        add = 0
        for x in rotated:
            add += int(x)
        sum += add
    if(equator[i] == "*"):
        multiply = int(rotated[0])
        for x in range(1, len(rotated)):
            multiply *= int(rotated[x])
        sum += multiply
        

print(sum)