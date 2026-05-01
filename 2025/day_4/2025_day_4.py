# Average time per: 14 minutes
grid = []
inputFile = open("2025/day_4/input.txt", "r")
for line in inputFile:
    line = line.strip()
    row = []
    for i in line:
        row.append(i)
    grid.append(row)
inputFile.close()

amount = 0
for i in range(25):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            adjac = 0
            if(grid[x][y] == "@"):
                if(x != 0 and y != 0):
                    if(grid[x - 1][y - 1] == "@"):
                        adjac += 1
                if(x != 0):
                    if(grid[x - 1][y] == "@"):
                        adjac += 1
                if(x != 0 and y != 137):
                    if(grid[x - 1][y + 1] == "@"):
                        adjac += 1
                if(y != 137):
                    if(grid[x][y + 1] == "@"):
                        adjac += 1
                if(x != 137 and y != 137):
                    if(grid[x + 1][y + 1] == "@"):
                        adjac += 1
                if(x != 137):
                    if(grid[x + 1][y] == "@"):
                        adjac += 1
                if(x != 137 and y != 0):
                    if(grid[x + 1][y - 1] == "@"):
                        adjac += 1
                if(y != 0):
                    if(grid[x][y - 1] == "@"):
                        adjac += 1
                
                if(adjac < 4):
                    # print(f"{x}, {y}")
                    amount += 1
                    grid[x][y] = "."
print(amount)