# Average time per: 18 minutes
part_1 = []
part_2 = []
fresh_find = True
check = []

inputFile = open("2025/day_5/input.txt", "r")
for line in inputFile:
    line = line.strip()
    if not line:
        fresh_find = False
    elif fresh_find:
        broken = line.split("-")
        part_1.append(int(broken[0]))
        part_2.append(int(broken[1]))
    else:
        check.append(int(line))
inputFile.close()




is_fresh = 0
# for i in range(min(part_1), max(part_2) + 1):
#     for j in range(len(part_1)):
#         if i >= part_1[j] and i <= part_2[j]:
#             is_fresh += 1
#             break
# print(is_fresh)

for _ in range(10):
    ranges = []
    for i in range(len(part_1)):
        added = False
        for j in range(len(ranges)):
            if(part_1[i] <= ranges[j][1] and part_2[i] >= ranges[j][1]):
                ranges[j][1] = part_2[i]
                added = True
            if(part_2[i] >= ranges[j][0] and part_1[i] <= ranges[j][0]):
                ranges[j][0] = part_1[i]
                added = True
            if(part_1[i] >= ranges[j][0] and part_2[i] <= ranges[j][1]):
                added = True
        if not added:
            ranges.append([part_1[i], part_2[i]])
    
    part_1 = []
    part_2 = []
    for i in range(len(ranges)):
        part_1.append(ranges[i][0])
        part_2.append(ranges[i][1])
        
sum = 0
for i in range(len(ranges)):
    sum += ranges[i][1] - ranges[i][0] + 1
        
print(sum)