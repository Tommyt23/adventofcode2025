from pathlib import Path

PICKS = 12


def max_joltage_for_bank(line: str, picks: int = PICKS) -> int:
    digits = [int(c) for c in line.strip()]
    if len(digits) < picks:
        return 0

    to_drop = len(digits) - picks
    stack: list[int] = []

    for digit in digits:
        while stack and to_drop > 0 and stack[-1] < digit:
            stack.pop()
            to_drop -= 1
        stack.append(digit)

    best_digits = stack[:picks]
    value = 0
    for digit in best_digits:
        value = value * 10 + digit
    return value


def load_input() -> list[str]:
    input_path = Path('src/day 3/data/day3.txt')
    return input_path.read_text().splitlines()


def solve(data: list[str]) -> int:
    total = 0
    for line in data:
        line = line.strip()
        if not line:
            continue
        total += max_joltage_for_bank(line)
    return total


if __name__ == '__main__':
    print(solve(load_input()))
