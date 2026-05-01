binary = []
buttons = []
voltages = []

inputFile = open("2025/day_10/input.txt", "r")
for line in inputFile:
    line = line.strip()
    line = line.split()
    
    list_buttons = []
    
    for i in line:
        if(i[0] != "{"):
            i = i[1:]
            i = i[:-1]

            if(i[0] == "." or i[0] == "#"):
                binary.append(i)
            else:
                list_buttons.append(i.split(","))
        else:
            voltages.append(i.split(","))
    buttons.append(list_buttons)
inputFile.close()


# def button_press(binary, button):
#     new_button = []
#     for i in button:
#         new_button.append(int(i))
        
#     new_binary = ""
#     for i in range(len(binary)):
#         if i not in new_button:
#             new_binary += binary[i]
            
#         else:
#             if binary[i] == ".":
#                 new_binary += "#"
#             else:
#                 new_binary += "."
                
#     return new_binary


# def find_min(binary, buttons):
#     count = 0
#     potential = [binary]
#     while ("." * len(binary)) not in potential:
#         new_potential = []
#         for i in potential:
#             for j in range(len(buttons)):
#                 if(button_press(i, buttons[j]) not in new_potential):
#                     new_potential.append(button_press(i, buttons[j]))
#                 # print(f"{button_press(i, buttons[j])}, {buttons[j]}")
#         potential = new_potential
#         count += 1
#         # print(count)
#     return count
            
            
# sum = 0
# for i in range(len(binary)):
#     print(i)
#     sum += find_min(binary[i], buttons[i])
# print(sum)



for i in range(len(voltages)):
    for j in range(len(voltages[i])):
        voltages[i][j] = voltages[i][j].replace("{", "")
        voltages[i][j] = voltages[i][j].replace("}", "")
        voltages[i][j] = int(voltages[i][j])
# print(voltages)



def button_press(voltage, button):
    # print(voltage)
    new_button = []
    for i in button:
        new_button.append(int(i))
        
    new_voltage = []
    for i in voltage:
        new_voltage.append(i)

    for i in new_button:
        new_voltage[i] += 1
        
                
    return new_voltage

# print(button_press(voltages[0], buttons[0][0]))
# print(voltages[0])

# def find_volt(voltage, buttons):
#     potential = [[0] * len(voltage)]
#     count = 0
#     while voltage not in potential:
#         new_potential = []
#         for i in potential:
#             for j in range(len(buttons)):
#                 if button_press(i, buttons[j]) not in new_potential:
#                     new_potential.append(button_press(i, buttons[j]))
#         potential = new_potential
#         count += 1
#         # print(len(potential))
#     return count
    


# for i in range(len(voltages)):
#     print(find_volt(voltages[i], buttons[i]))

# print(voltages[7])
# print(find_volt(voltages[7], buttons[7]))


# test 0: 10
# test 1: 12
# test 2: 11
# input 7: 23


# def bet_sort(buttons):
#     new_buttons = []
#     while buttons != []:
#         max_len = max(buttons, key=len)
#         new_buttons.append(max_len)
#         buttons.remove(max_len)
#     buttons = new_buttons
#     return buttons
# print(bet_sort(buttons[1]))

finder = [0] * len(voltages[0])
print(finder)

print(buttons[0])
for i in buttons[0]:
    for j in i:
        finder[int(j)] += 1
        
print(finder)

new_volt = [0] * len(voltages[0])
for i in finder:
    if i == 1:
        for j in buttons[0]:
            if str(i) in j:
                while new_volt[i] != voltages[0][i]:
                    new_volt = button_press(new_volt, j)
                    print(new_volt)