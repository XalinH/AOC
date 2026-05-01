letter_list = []
inputFile = open("2022/day_6/input.txt", "r")
for line in inputFile:
    for x in range(len(line)):
        letter_list.append(line[x])
inputFile.close()

# counter = 2
counter = 12
running = True

if(letter_list[0] == letter_list[1] or letter_list[1] == letter_list[2] or letter_list[2] == letter_list[0]):
    running = False

while running:
    counter += 1
    if(counter == len(letter_list)):
        running = False
    # elif(letter_list[counter] != letter_list[counter - 1] and
    # letter_list[counter] != letter_list[counter - 2] and
    # letter_list[counter] != letter_list[counter - 3] and
    # letter_list[counter - 1] != letter_list[counter - 2] and
    # letter_list[counter - 1] != letter_list[counter - 3] and
    # letter_list[counter - 2] != letter_list[counter - 3]):
    #     running = False
    part = []
    for i in range(counter - 13, counter):
        part.append(letter_list[i])
    part.sort()
    
    found = False
    for i in range(len(part) - 1):
        if(part[i] == part[i + 1]):
            found = True
    if not found:
        running = False
        
print(counter + 1)