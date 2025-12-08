import math

with open("input.txt", "rt") as file:
    lines = file.read().strip().split("\n")

data = [tuple(map(int, line.split(","))) for line in lines]

def dist(coord1, coord2):
    return math.sqrt(
        (coord1[0] - coord2[0]) ** 2 + 
        (coord1[1] - coord2[1]) ** 2 + 
        (coord1[2] - coord2[2]) ** 2
    )

distances = [(dist(data[i], data[j]), (i, j)) for i in range(len(data)) for j in range(i + 1, len(data))]
distances.sort(key=lambda x: x[0])

def count_components(graph):
    visited = set()
    components = []
    
    for node in graph:
        if node not in visited:
            stack = [node]
            visited.add(node)
            size = 0
            
            while stack:
                current = stack.pop()
                size += 1
                
                for neighbor in graph[current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        stack.append(neighbor)
            
            components.append(size)
            if len(components) > 1:
                return False

    return len(components) == 1


result = 0
graph = {i: set() for i in range(len(data))}
for d, (i, j) in distances:
    graph[i].add(j)
    graph[j].add(i)
    
    is_ = count_components(graph)
    if is_:
        result = data[i][0] * data[j][0]
        break


print(result)