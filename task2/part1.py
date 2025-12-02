with open("input.txt", "r") as file:
    ranges = file.read().strip().split(",")


counter = 0
for rang in ranges:
    start, end = map(int, rang.split("-"))
    for num in range(start, end + 1):
        string = str(num)
        if len(string) % 2 == 0 and string[:len(string) // 2] == string[len(string) // 2:]:
            counter += num

print(counter)
            