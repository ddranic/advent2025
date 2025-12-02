with open("input.txt", "r") as file:
    ranges = file.read().strip().split(",")


def is_invalid(num: int) -> bool:
    string = str(num)
    for i in range(1, len(string) // 2 + 1):
        if len(string) % i == 0:
            if string[:i] * (len(string) // i) == string:
                return True
    return False


counter = 0
for rang in ranges:
    start, end = map(int, rang.split("-"))
    for num in range(start, end + 1):
        if is_invalid(num):
            counter += num

print(counter)
            