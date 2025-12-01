with open("input.txt", "r") as file:
    lines = file.readlines()

counter = 0
current = 50
for line in lines:
    line = line.strip()

    rotation = line[0]
    degrees = int(line[1:])

    if rotation == "L":
        current = (current - degrees) % 100
    elif rotation == "R":
        current = (current + degrees) % 100
    
    if current == 0:
        counter += 1

print(counter)