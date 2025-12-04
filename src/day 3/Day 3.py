def max_joltage_for_bank(line: str) -> int:
    digits = [int(c) for c in line.strip()]
    if len(digits) < 2:
        return 0

    best_right = -1
    best_value = -1

    for d in reversed(digits):
        if best_right != -1:
            candidate = 10 * d + best_right
            if candidate > best_value:
                best_value = candidate
        if d > best_right:
            best_right = d

    return best_value


def total_output_joltage(filename: str) -> int:
    total = 0
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue  # skip blank lines
            total += max_joltage_for_bank(line)
    return total


if __name__ == "__main__":
    print(total_output_joltage("src/day 3/data/day3.txt"))
