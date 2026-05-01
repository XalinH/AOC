inputFile = open("2024/day_11/input.txt", "r")
for line in inputFile:
    line = line.strip()
    numbers = line.split()
inputFile.close()

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
    
for _ in range(75):
    new_numbers = []
    for i in range(len(numbers)):
        if numbers[i] == 0:
            new_numbers.append(1)
        elif len(str(numbers[i])) % 2 == 0:
            string_ver = str(numbers[i])
            half_point = int(len(string_ver) / 2)
            split1 = string_ver[:half_point]
            split2 = string_ver[half_point:]
            new_numbers.append(int(split1))
            new_numbers.append(int(split2))
        else:
            new_numbers.append(numbers[i] * 2024)
    
    
    numbers = new_numbers
    
print(len(numbers))