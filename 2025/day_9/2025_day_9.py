xs = []
ys = []
inputFile = open("2025/day_9/input.txt", "r")
for line in inputFile:
    line = line.strip()
    line = line.split(",")
    xs.append(int(line[0]))
    ys.append(int(line[1]))
inputFile.close()

solutions = []
for i in range(len(xs) - 1):
    for j in range(i, len(xs)):
        solutions.append((abs(xs[i] - xs[j]) + 1) * (abs(ys[i] - ys[j]) + 1))
        
# grid = []
# for i in range(max(ys)):
#     row = []
#     for j in range(max(xs)):
#         row.append(".")
#     grid.append(row)
# for i in range(len(xs) - 1):
#     if(ys[i] == ys[i + 1]):
#         if(xs[i] > xs[i + 1]):
#             for j in range(xs[i + 1] - 1, xs[i]):
#                 grid[ys[i] - 1][j] = "#"
#         if(xs[i] < xs[i + 1]):
#             for j in range(xs[i] - 1, xs[i + 1]):
#                 grid[ys[i] - 1][j] = "#"
98242
grid = []
for i in range(max(ys)):
    print(i)
    row = []
    for j in range(max(xs)):
        row.append(".")
    grid.append(row)
for i in range(len(xs)):
    grid[ys[i] - 1][xs[i] - 1] = "#"
    
# for i in range(len(grid)):
#     for j in range(len(grid[i])):
#         print(grid[i][j], end="")
#     print()

solutions.sort()
print(solutions[-1])