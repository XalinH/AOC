do = ["noop"]
add = [0]
# 14220
inputFile = open("2022/day_10/input.txt", "r")
for line in inputFile:
    line = line.strip()
    broken = line.split()
    if(broken[0] == 'addx'):
        do.append("noop")
        add.append(0)
    do.append(broken[0])
    if(len(broken) > 1):
        add.append(int(broken[1]))
    else:
        add.append(0)
inputFile.close()

x = 1
list_rounds = []
for i in range(len(do)):
    if(do[i] == "addx"):
        x += add[i]
    list_rounds.append(x)
print(list_rounds)
print(list_rounds[20])
print(list_rounds[60])
print(list_rounds[100])
print(list_rounds[140])
print(list_rounds[180])
print(list_rounds[220])
i = 0
for a in list_rounds:
    print(f"{i}: {a}")
    i += 1
sum = list_rounds[19] * 20 + list_rounds[59] * 60 + list_rounds[99] * 100
sum += list_rounds[139] * 140 + list_rounds[179] * 180 + list_rounds[219] * 220
print(sum)