# Average time per: 22 minutes
broken = []
inputFile = open("2025/day_2/input.txt", "r")
for line in inputFile:
    line = line.strip()
    part_broken = line.split(",")
    # print(part_broken)
    for i in range(len(part_broken)):
        broken.append(part_broken[i].split("-"))
inputFile.close()
# print(broken[0][0])
sum = 0
for i in range(len(broken)):
    for j in range(int(broken[i][0]), int(broken[i][1])):
        string_j = str(j)
        for i in range(len(string_j) - 1):
            sub_string = string_j[:i]
            if(string_j.replace(sub_string, "") == ""):
                sum += j
                # print(j)
                break

print(sum)