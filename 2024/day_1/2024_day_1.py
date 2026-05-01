col_1 = []
col_2 = []
inputFile = open("2024/day_1/input.txt", "r")
for line in inputFile:
    line = line.strip()
    broken = line.split()
    col_1.append(int(broken[0]))
    col_2.append(int(broken[1]))
inputFile.close()

col_1.sort()
col_2.sort()

sum = 0
for i in range(len(col_1)):
    sum += abs(col_1[i] - col_2[i])
print(sum)


# sum = 0
# for i in range(len(col_1)):
#     sum += col_1[i] * col_2.count(col_1[i])
# print(sum)