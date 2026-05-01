p1_sec_1 = []
p1_sec_2 = []
p2_sec_1 = []
p2_sec_2 = []

inputFile = open("2022/day_4/input.txt", "r")
for line in inputFile:
    sep = line.split('-')
    sep2 = sep[1].split(',')
    p1_sec_1.append(int(sep[0]))
    p1_sec_2.append(int(sep2[0]))
    p2_sec_1.append(int(sep2[1]))
    p2_sec_2.append(int(sep[2].strip()))
inputFile.close()

sum = 0
for i in range(len(p1_sec_1)):
    if(p1_sec_1[i] <= p2_sec_1[i] and p1_sec_2[i] >= p2_sec_2[i]):
        sum += 1
    elif(p1_sec_1[i] >= p2_sec_1[i] and p1_sec_2[i] <= p2_sec_2[i]):
        sum += 1
print(sum)


sum = 0
for i in range(len(p1_sec_1)):
    if(p1_sec_1[i] <= p2_sec_1[i] and p1_sec_2[i] >= p2_sec_1[i] or p2_sec_1[i] <= p1_sec_1[i] and p2_sec_2[i] >= p1_sec_1[i]):
        sum += 1
    elif(p1_sec_1[i] <= p2_sec_2[i] and p1_sec_2[i] >= p2_sec_2[i] or p2_sec_1[i] <= p1_sec_2[i] and p2_sec_2[i] >= p1_sec_2[i]):
        sum += 1
print(sum)