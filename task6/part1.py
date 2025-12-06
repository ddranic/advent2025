with open("input.txt", "rt") as file:
    lines = file.read().strip().split("\n")
table = [line.split() for line in lines]

result = 0
for j in range(len(table[0])):
    op = table[-1][j]
    nums = [int(table[i][j]) for i in range(len(table) - 1)]
    if op == "+":
        result += sum(nums)
    elif op == "*":
        r = 1
        for n in nums:
            r *= n
        result += r

print(result)
