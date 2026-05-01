grid = []
grid2 = []
inputFile = open("2024/day_6/input.txt", "r")
for line in inputFile:
    line = line.strip()
    row = []
    for i in line:
        row.append(i)
    grid.append(row)
    grid2.append(row)
inputFile.close()

direction = "U"
guard = []
guard2 = []
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if(grid[i][j] == "^"):
            guard = [i, j]
            guard2 = [i, j]
print(guard)


places_been = []
i = 0
while(guard[0] != -1 and guard[1] != -1 and guard[0] != 130 and guard[1] != 130):
    if guard not in places_been:
        places_been.append(guard)
        
    if(direction == "U"):
        if(guard[0] - 1 != -1 and grid[guard[0] - 1][guard[1]] == "#"):
            direction = "R"
        else:
            guard = [guard[0] - 1, guard[1]]
            
    elif(direction == "D"):
        if(guard[0] + 1 != 130 and grid[guard[0] + 1][guard[1]] == "#"):
            direction = "L"
        else:
            guard = [guard[0] + 1, guard[1]]
            
    elif(direction == "R"):
        if(guard[1] + 1 != 130 and grid[guard[0]][guard[1] + 1] == "#"):
            direction = "D"
        else:
            guard = [guard[0], guard[1] + 1]
            
    elif(direction == "L"):
        if(guard[1] - 1 != -1 and grid[guard[0]][guard[1] - 1] == "#"):
            direction = "U"
        else:
            guard = [guard[0], guard[1] - 1]
    i += 1
print(places_been)
print(len(places_been))

ob = 0
for i in range(len(places_been)):
    grid = grid2.copy()
    print(grid[places_been[i][0]][places_been[i][1]])
    print(grid2[places_been[i][0]][places_been[i][1]])
    grid[places_been[i][0]][places_been[i][1]] = "#"
    if(grid != grid2):
        print("A")
    loop = 0
    guard = guard2
    places_been_2 = []
    while((guard[0] != -1 and guard[1] != -1 and guard[0] != 130 and guard[1] != 130) and loop < 1000):
        if guard not in places_been_2:
            places_been_2.append(guard)
            loop = 0
            # print("A")
        else:
            loop += 1
            
        if(direction == "U"):
            if(guard[0] - 1 != -1 and grid[guard[0] - 1][guard[1]] == "#"):
                direction = "R"
            else:
                guard = [guard[0] - 1, guard[1]]
                
        elif(direction == "D"):
            if(guard[0] + 1 != 130 and grid[guard[0] + 1][guard[1]] == "#"):
                direction = "L"
            else:
                guard = [guard[0] + 1, guard[1]]
                
        elif(direction == "R"):
            if(guard[1] + 1 != 130 and grid[guard[0]][guard[1] + 1] == "#"):
                direction = "D"
            else:
                guard = [guard[0], guard[1] + 1]
                
        elif(direction == "L"):
            if(guard[1] - 1 != -1 and grid[guard[0]][guard[1] - 1] == "#"):
                direction = "U"
            else:
                guard = [guard[0], guard[1] - 1]
    if(loop >= 1000):
        ob += 1
    # print("isrunning")
print(ob)