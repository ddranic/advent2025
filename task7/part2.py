with open("input.txt", "rt") as file:
    lines = file.read().strip().split("\n")

table = [list(line) for line in lines]
height = len(table)
width = len(table[0])

graph = {} 
stack = [(lines[0].index("S"), 0, "S")]

while stack:
    x, y, p = stack.pop()
    if x < 0 or x >= width:
        continue
    while y < height:
        if table[y][x] == "." or table[y][x] == "S":
            y += 1
        if table[y][x] == "^":
            if p not in graph:
                graph[p] = []
            graph[p].append((x, y))
            if (x, y) not in graph:
                graph[(x, y)] = []
                stack.append((x - 1, y, (x, y)))
                stack.append((x + 1, y, (x, y)))
            break
    else:
        if p not in graph:
            graph[p] = []
        graph[p].append("F")

# DP to count paths
# I could actually use matrix exponentiation here
# Cause it is O(log n) instead of O(n)
# But i am too lazy to implement it now :/
dp = {}
def count(node):
    if node == "F":
        return 1
    if node in dp:
        return dp[node]
    dp[node] = sum(count(n) for n in graph[node])
    return dp[node]

print(count("S"))