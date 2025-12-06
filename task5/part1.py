with open("input.txt", "rt") as file:
    f = file.read().strip().split("\n\n")
    lines, ids = f[0].split("\n"), f[1].split("\n")

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

ans = 0
for x in ids:
    x = int(x)
    for a, b in merged:
        if a <= x <= b:
            ans += 1
            break
        if a > x:
            break

print(ans)