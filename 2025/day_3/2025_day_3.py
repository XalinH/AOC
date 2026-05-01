# Average time per: 18 minutes
batteries = []
inputFile = open("2025/day_3/input.txt", "r")
for line in inputFile:
    line = line.strip()
    row = []
    for i in line:
        row.append(int(i))
    batteries.append(row)
inputFile.close()

voltage = 0
for i in range(len(batteries)):
    highest = 0
    for j in range(len(batteries[i]) - 11):
        if(batteries[i][j] > batteries[i][highest]):
            highest = j
    second = highest + 1
    for j in range(highest + 1, len(batteries[i]) - 10):
        if(batteries[i][j] > batteries[i][second]):
            second = j
    third = second + 1
    for j in range(second + 1, len(batteries[i]) - 9):
        if(batteries[i][j] > batteries[i][third]):
            third = j
    fourth = third + 1
    for j in range(third + 1, len(batteries[i]) - 8):
        if(batteries[i][j] > batteries[i][fourth]):
            fourth = j
    fifth = fourth + 1
    for j in range(fourth + 1, len(batteries[i]) - 7):
        if(batteries[i][j] > batteries[i][fifth]):
            fifth = j
    sixth = fifth + 1
    for j in range(fifth + 1, len(batteries[i]) - 6):
        if(batteries[i][j] > batteries[i][sixth]):
            sixth = j
    seventh = sixth + 1
    for j in range(sixth + 1, len(batteries[i]) - 5):
        if(batteries[i][j] > batteries[i][seventh]):
            seventh = j
    eigth = seventh + 1
    for j in range(seventh + 1, len(batteries[i]) - 4):
        if(batteries[i][j] > batteries[i][eigth]):
            eigth = j
    ninth = eigth + 1
    for j in range(eigth + 1, len(batteries[i]) - 3):
        if(batteries[i][j] > batteries[i][ninth]):
            ninth = j
    tenth = ninth + 1
    for j in range(ninth + 1, len(batteries[i]) - 2):
        if(batteries[i][j] > batteries[i][tenth]):
            tenth = j
    eleventh = tenth + 1
    for j in range(tenth + 1, len(batteries[i]) - 1):
        if(batteries[i][j] > batteries[i][eleventh]):
            eleventh = j
    twelth = eleventh + 1
    for j in range(eleventh + 1, len(batteries[i])):
        if(batteries[i][j] > batteries[i][twelth]):
            twelth = j
    combined_str = str(batteries[i][highest]) 
    combined_str += str(batteries[i][second])
    combined_str += str(batteries[i][third])
    combined_str += str(batteries[i][fourth])
    combined_str += str(batteries[i][fifth])
    combined_str += str(batteries[i][sixth])
    combined_str += str(batteries[i][seventh])
    combined_str += str(batteries[i][eigth])
    combined_str += str(batteries[i][ninth])
    combined_str += str(batteries[i][tenth])
    combined_str += str(batteries[i][eleventh])
    combined_str += str(batteries[i][twelth])
    combined_int = int(combined_str)
    voltage += combined_int
    print(combined_int)
print(voltage)