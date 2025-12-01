with open("input.txt", "r") as file:
    lines = file.readlines()

counter = 0
current = 50
for line in lines:
    line = line.strip()

    rotation = line[0]
    degrees = int(line[1:])

    if rotation == "L":
        need_to_zero = current if current > 0 else 100
        if degrees < need_to_zero:
            current = (current - degrees) % 100
            continue

        counter += 1 + (degrees - need_to_zero) // 100
        current = (current - degrees) % 100

    elif rotation == "R":
        need_to_zero = 100 - current if current > 0 else 100
        if degrees < need_to_zero:
            current = (current + degrees) % 100
            continue

        counter += 1 + (degrees - need_to_zero) // 100
        current = (current + degrees) % 100
    

print(counter)