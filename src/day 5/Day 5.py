from pathlib import Path


def load_input() -> list[str]:
    input_path = Path('src/day 5/data/day5.txt')
    return input_path.read_text().splitlines()


def solve(data: list[str]) -> int:
    ranges: list[tuple[int, int]] = []
    ids: list[int] = []

    parsing_ranges = True
    for line in data:
        line = line.strip()
        if not line:
            parsing_ranges = False
            continue
        if parsing_ranges:
            start_str, end_str = line.split("-")
            start = int(start_str)
            end = int(end_str)
            if start > end:
                start, end = end, start
            ranges.append((start, end))
        else:
            ids.append(int(line))

    fresh_count = 0
    for value in ids:
        for start, end in ranges:
            if start <= value <= end:
                fresh_count += 1
                break

    return fresh_count


if __name__ == '__main__':
    print(solve(load_input()))
