import math
xs = []
ys = []
zs = []
inputFile = open("2025/day_8/input.txt", "r")
for line in inputFile:
    line = line.strip()
    line = line.split(",")
    xs.append(int(line[0]))
    ys.append(int(line[1]))
    zs.append(int(line[2]))
inputFile.close()

def find_dist(box1, box2):
    result = math.sqrt((xs[box1] - xs[box2]) ** 2 + (ys[box1] - ys[box2]) ** 2 + (ys[box1] - ys[box2]) ** 2)
    return result
    
list_dist = []
for i in range(len(xs) - 1):
    for j in range(i + 1, len(xs)):
        list_dist.append([i, j, find_dist(i, j)])

find_lowest = sorted(list_dist, key=lambda sublist: sublist[2])
for i in find_lowest:
    print(i)

circuits = []
for i in range(10):
    circuits.append([find_lowest[i][0], find_lowest[i][1]])
    
for i in range(len(circuits)):
    circuits[i].sort()
circuits = sorted(circuits, key=lambda sublist: sublist[0])


# new_list = []
# for i in range(1000):
#     new_list.append([i])
# for i in range(1000):
#     for j in circuits:
#         if i == j[0]:
#             new_list[i].append(j[1])
#         if i == j[1]:
#             new_list[i].append(j[0])
        
print(circuits)

newer_list = []
for i in circuits:
    newer_list.append(i[0])
    newer_list.append(i[1])
print(set(newer_list))
1, 9
5, 7, 19, 14
10, 12
11, 16
13, 17, 18

print(xs[19], ys[19], zs[19])