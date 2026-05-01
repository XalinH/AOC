rows = []
inputFile = open("2024/day_2/input.txt", "r")
for line in inputFile:
    line = line.strip()
    line = line.split()
    row = []
    for i in range(len(line)):
        row.append(int(line[i]))
    rows.append(row)
inputFile.close()
# print(rows)

safe_num = 0
for i in rows:
    safe = 0
    if(i[0] - i[1] > 0):
        ascending = False
    else:
        ascending = True
    j = 0
    
    while j < len(i) - 1:
        if((i[j] - i[j + 1] < 1 or i[j] - i[j+1] > 3) and not ascending):
            safe += 1
            i.pop(j)
        elif((i[j + 1] - i[j] < 1 or i[j + 1] - i[j] > 3) and ascending):
            safe += 1
            i.pop(j)
        else:
            j += 1
    
    if safe <= 0:
        # if(safe == 1):
            # print(i)
        safe_num += 1
print(safe_num)