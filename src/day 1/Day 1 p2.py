with open("src/day 1/data/day1.txt", "r") as f:
    lines = f.readlines()

count = 0
value = 50
m = 100  # dial size

for line in lines:
    line = line.strip()
    if not line:
        continue

    direction = line[0]
    dist = int(line[1:])

    step = 1 if direction == "R" else -1

    # Simulate every click (safe because AoC input distances are not huge)
    for _ in range(dist):
        value = (value + step) % m
        if value == 0:
            count += 1

print(count)

