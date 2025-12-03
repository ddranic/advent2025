with open("input.txt", mode="rt") as file:
    lines = file.readlines()

digits = ["9", "8", "7", "6", "5", "4", "3", "2", "1", "0"]

counter = 0
for line in lines:
    line = line.strip()
    for dig in digits:
        idx = line.find(dig)
        if idx == len(line) - 1:
            continue
        if idx != -1:
            for nest_dig in digits:
                nest_idx = line.find(nest_dig, idx + 1)
                if nest_idx != -1:
                    counter += int(dig + nest_dig)
                    break
            break

print(counter)
