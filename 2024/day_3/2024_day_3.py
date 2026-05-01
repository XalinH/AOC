rows = ""
inputFile = open("2024/day_3/input.txt", "r")
for line in inputFile:
    line = line.strip()
    rows += line
inputFile.close()

bef_list = rows.split("don't")
print(bef_list)

new_list = rows.split("mul(")
new_list.pop(0)
# print(new_list)

sum = 0
for i in range(len(new_list)):
    for j in range(len(new_list[i])):
        if new_list[i][j] == ")":
            new_list[i] = new_list[i][:j]
            break
            
    print(new_list[i])
    spliter = new_list[i].split(",")
    if(len(spliter) == 2):
        if spliter[0].isdigit() and spliter[1].isdigit():
            sum += int(spliter[0]) * int(spliter[1])
        
print(sum)