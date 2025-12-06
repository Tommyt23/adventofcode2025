from pathlib import Path


def load_input() -> list[str]:
    input_path = Path('src/day 5/data/day5.txt')
    return input_path.read_text().splitlines()


def solve(data: list[str]) -> int:
    ranges: list[tuple[int, int]] = []

    for line in data:
        line = line.strip()
        if not line:
            break
        start_str, end_str = line.split("-")
        start = int(start_str)
        end = int(end_str)
        if start > end:
            start, end = end, start
        ranges.append((start, end))

    if not ranges:
        return 0

    ranges.sort()
    merged: list[tuple[int, int]] = []
    cur_start, cur_end = ranges[0]
    for start, end in ranges[1:]:
        if start <= cur_end + 1:
            if end > cur_end:
                cur_end = end
        else:
            merged.append((cur_start, cur_end))
            cur_start, cur_end = start, end
    merged.append((cur_start, cur_end))

    total = 0
    for start, end in merged:
        total += end - start + 1
    return total


if __name__ == '__main__':
    print(solve(load_input()))
