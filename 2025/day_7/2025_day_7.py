grid = []
inputFile = open("2025/day_7/input.txt", "r")
for line in inputFile:
    line = line.strip()
    row = []
    for i in line:
        row.append(i)
    grid.append(row)
inputFile.close()
# print(grid)
for i in range(len(grid[0])):
    if(grid[0][i] =="S"):
        s_pos = i

times_hit = 0
areas_search = [s_pos]
for i in range(1, len(grid)):
    for j in range(len(grid[i])):
        for k in range(len(areas_search)):
            if(grid[i][j] == "^" and areas_search[k] == j):
                times_hit += 1
                if areas_search[k] - 1 not in areas_search:
                    areas_search.append(areas_search[k] - 1)
                if areas_search[k] + 1 not in areas_search:
                    areas_search.append(areas_search[k] + 1)
                areas_search.pop(k)
                j += 1
                break
            # else:
            #     grid[i][j] = "&"
                
print(times_hit)
print(areas_search)
# print(grid[:5])

# areas_searc = [s_pos]
# timelines = 0

# def splits(areas_search, row):
#     global timelines
#     for i in range(row, len(grid)):
#         for j in range(len(grid[row])):
#             if(grid[i][j] == "^" and j in areas_search):
#                 areas_search.remove(j)
#                 areas_search.append(j - 1)
#                 splits(areas_search, i)
#                 areas_search.pop()
#                 areas_search.append(j + 1)
#                 splits(areas_search, i)
#     timelines += 1

# splits(areas_searc, 1)
# print(timelines)

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if(grid[i][j] == "."):
            grid[i][j] = 0

grid[1][s_pos] = 1
print(grid[0][7])
print(grid[1][7])
a = 0
for i in range(2, len(grid)):
    for j in range(len(grid[i])):
        print(a)
        if(j > 0 and grid[i][j - 1] == "^"):
            grid[i][j] += grid[i - 1][j - 1]
        if(j < len(grid[i]) - 1 and grid[i][j + 1] == "^"):
            grid[i][j] += grid[i - 1][j + 1]
        if(grid[i - 1][j] != "^" and grid[i][j] != "^"):
            grid[i][j] += grid[i - 1][j]
        a += 1

for i in range(len(grid)):
    print(grid[i])

sum = 0
for i in grid[len(grid) - 1]:
    sum += i
print(sum)