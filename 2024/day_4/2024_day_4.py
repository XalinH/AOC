grid = []
inputFile = open("2024/day_4/input.txt", "r")
for line in inputFile:
    line = line.strip()
    row = []
    for i in range(len(line)):
        row.append(line[i])
    grid.append(row)
inputFile.close()
print(grid)

counted = 0
for y in range(140):
    for x in range(140):
        # if(grid[x][y] == "X"):
        #     if(x + 3 < 140 and y + 3 < 140):
        #         if(grid[x + 1][y + 1] == "M" and grid[x + 2][y + 2] == "A" and grid[x + 3][y + 3] == "S"):
        #             counted += 1
        #     if(x + 3 < 140):
        #         if(grid[x + 1][y] == "M" and grid[x + 2][y] == "A" and grid[x + 3][y] == "S"):
        #             counted += 1
        #     if(y + 3 < 140):
        #         if(grid[x][y + 1] == "M" and grid[x][y + 2] == "A" and grid[x][y + 3] == "S"):
        #             counted += 1
        #     if(x - 3 > -1 and y - 3 > -1):
        #         if(grid[x - 1][y - 1] == "M" and grid[x - 2][y - 2] == "A" and grid[x - 3][y - 3] == "S"):
        #             counted += 1
        #     if(x - 3 > -1):
        #         if(grid[x - 1][y] == "M" and grid[x - 2][y] == "A" and grid[x - 3][y] == "S"):
        #             counted += 1
        #     if(y - 3 > -1):
        #         if(grid[x][y - 1] == "M" and grid[x][y - 2] == "A" and grid[x][y - 3] == "S"):
        #             counted += 1
        #     if(x - 3 > -1 and y + 3 < 140):
        #         if(grid[x - 1][y + 1] == "M" and grid[x - 2][y + 2] == "A" and grid[x - 3][y + 3] == "S"):
        #             counted += 1
        #     if(x + 3 < 140 and y - 3 > -1):
        #         if(grid[x + 1][y - 1] == "M" and grid[x + 2][y - 2] == "A" and grid[x + 3][y - 3] == "S"):
        #             counted += 1
        if(grid[x][y] == "A" and x != 0 and y != 0 and x != 139 and y != 139):
            down_up = False
            up_down = False
            if(grid[x + 1][y - 1] == "S" and grid[x - 1][y + 1] == "M" or grid[x + 1][y - 1] == "M" and grid[x - 1][y + 1] == "S"):
                down_up = True
            if(grid[x + 1][y + 1] == "S" and grid[x - 1][y - 1] == "M" or grid[x + 1][y + 1] == "M" and grid[x - 1][y - 1] == "S"):
                up_down = True
            if down_up and up_down:
                counted += 1
                    
print(counted)