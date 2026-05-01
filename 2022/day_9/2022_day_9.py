import copy

direction = []
spaces = []
inputFile = open("2022/day_9/input.txt", "r")
for line in inputFile:
    line = line.strip()
    broken = line.split()
    direction.append(broken[0])
    spaces.append(int(broken[1]))
inputFile.close()


h_spot = [0, 0]
t_spot = [0, 0]
list_spots = [[0, 0]]
first_10 = 0
for i in range(len(direction)):
    if(direction[i] == "L"):
        for j in range(spaces[i]):
            h_spot[0] -= 1
            if(abs(h_spot[0] - t_spot[0]) > 9):
                t_spot[0] = h_spot[0] + 9
                # t_spot[1] = h_spot[1]
                list_spots.append([int(t_spot[0]), int(t_spot[1])])
            if(first_10 < 100):
                print(f"{t_spot}, {h_spot}")
    if(direction[i] == "R"):
        for j in range(spaces[i]):
            h_spot[0] += 1
            if(abs(h_spot[0] - t_spot[0]) > 9):
                t_spot[0] = h_spot[0] - 9
                # t_spot[1] = h_spot[1]
                list_spots.append([int(t_spot[0]), int(t_spot[1])])
            if(first_10 < 100):
                print(f"{t_spot}, {h_spot}")
    if(direction[i] == "U"):
        for j in range(spaces[i]):
            h_spot[1] -= 1
            if(abs(h_spot[1] - t_spot[1]) > 9):
                # t_spot[0] = h_spot[0]
                t_spot[1] = h_spot[1] + 9
                list_spots.append([int(t_spot[0]), int(t_spot[1])])
            if(first_10 < 100): 
                print(f"{t_spot}, {h_spot}")
    if(direction[i] == "D"):
        for j in range(spaces[i]):
            h_spot[1] += 1
            if(abs(h_spot[1] - t_spot[1]) > 9):
                # t_spot[0] = h_spot[0]
                t_spot[1] = h_spot[1] - 9
                list_spots.append([int(t_spot[0]), int(t_spot[1])])
            if(first_10 < 100):
                print(f"{t_spot}, {h_spot}")
    # print(t_spot)
    first_10 += 1
         
print(f"{t_spot}, {h_spot}")           
# print(list_spots)
print(len(list_spots))
new_list = []
for i in list_spots:
    if i not in new_list:
        new_list.append(i)
print(len(new_list))
    
print(new_list[0:10])