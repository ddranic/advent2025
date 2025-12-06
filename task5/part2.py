with open("input.txt", "rt") as file:
    f = file.read().strip().split("\n\n")
    lines = f[0].split("\n")

ranges = []
for line in lines:
    a, b = line.split("-")
    ranges.append((int(a), int(b)))

ranges.sort()

merged = []
for a, b in ranges:
    if not merged:
        merged.append((a, b))
        continue
    x, y = merged[-1]
    if a <= y + 1:
        merged[-1] = (x, max(y, b))
    else:
        merged.append((a, b))

rsult = 0
for a, b in merged:
    rsult += b - a + 1

print(rsult)
