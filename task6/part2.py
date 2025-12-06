with open("input.txt", "rt") as file:
    lines = file.read().split("\n")

while lines[-1] == "":
    lines.pop()

w = max(len(s) for s in lines)
lines = [s.ljust(w) for s in lines]

result = 0
nums = []

for col in range(w - 1, -1, -1):
    all_space = True
    for row in range(len(lines)):
        if lines[row][col] != ' ':
            all_space = False
            break

    if all_space:
        continue

    dig = str()
    for row in range(len(lines) - 1):
        if lines[row][col].isdigit():
            dig += lines[row][col]

    if dig:
        nums.append(int(dig))

    op = lines[-1][col]
    if op == '+':
        result += sum(nums)
        nums = []
    elif op == '*':
        r = 1
        for n in nums:
            r *= n
        result += r
        nums = []

print(result)
