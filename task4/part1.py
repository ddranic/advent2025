with open("input.txt", mode="rt") as file:
    lines = file.readlines()

table = [list(line.strip()) for line in lines]

rows = len(table)
cols = len(table[0])

directions = [
    (-1, -1), 
    (-1, 0), 
    (-1, 1),
    (0, -1),  
    (0, 1),
    (1, -1),  
    (1, 0), 
    (1, 1)
]


counter = 0
while True:
    flag = False
    for r in range(rows):
        for c in range(cols):
            if table[r][c] == '@':
                neighbor_count = 0
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and table[nr][nc] == '@':
                        neighbor_count += 1
                
                if neighbor_count <= 3:
                    flag = True
                    counter += 1
    if not flag:
        break
    
print(counter)