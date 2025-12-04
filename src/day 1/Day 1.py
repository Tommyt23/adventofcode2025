with open("src/day 1/data/day1.txt", "r") as f:
    lines = f.readlines()

count = 0
value = 50
first_chars = []
for line in lines:
    if line[0] == "L":
        value -= int(line[1:])
    elif line[0] == "R":
        value += int(line[1:])
    while value < 0:
        value += 100
    while value >= 100:
        value -= 100
    
    if value == 0:
        count += 1

print(count)
