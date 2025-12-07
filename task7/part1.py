with open("input.txt", "rt") as file:
    lines = file.read().strip().split("\n")

table = [list(line) for line in lines]
height = len(table)
width = len(table[0])

visited = set()
stack = [(lines[0].index("S"), 0)]

while stack:
    x, y = stack.pop()
    if x < 0 or x >= width:
        continue
    while y < height:
        if table[y][x] == "." or table[y][x] == "S":
            y += 1
        if table[y][x] == "^":
            if (x, y) not in visited:
                visited.add((x, y))
                stack.append((x - 1, y))
                stack.append((x + 1, y))
            break

print(len(visited))