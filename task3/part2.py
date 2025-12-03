with open("input.txt", mode="rt") as file:
    lines = file.readlines()

digits = ["9", "8", "7", "6", "5", "4", "3", "2", "1", "0"]

counter = 0

def find_max(line, start, length):
    if length == 0:
        return str()
    
    for dig in digits:
        idx = line.find(dig, start)
        if idx == -1 or idx >= len(line) - length + 1:
            continue
        nest_result = find_max(line, idx + 1, length - 1)
        if nest_result is not None:
            return dig + nest_result
        
    return None


for line in lines:
    line = line.strip()
    result = find_max(line, 0, 12)
    counter += int(result)

print(counter)
