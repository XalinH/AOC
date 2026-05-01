direction = []
amount = []
inputFile = open("2025/day_1/input.txt", "r")
for line in inputFile:
    line = line.strip()
    direction.append(line[0])
    amount.append(int(line[1:len(line)]))
inputFile.close()

hit = []
dial = 50
for i in range(len(direction)):
    last = False
    if(direction[i] == "R"):
        for i in range(amount[i]):
            dial += 1
            if(dial > 99):
                dial = 0
            # Comment out this part
            # if(dial == 0):
            #     hit.append(0)
    else:
        for i in range(amount[i]):
            dial -= 1
            if(dial < 0):
                dial = 99
            # Comment out this part
            # if(dial == 0):
            #     hit.append(0)
    # Comment out this part
    if(dial == 0):
        hit.append(0)

print(hit.count(0))
print(dial)