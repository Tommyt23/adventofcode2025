def is_invalid_id(n: int) -> bool:
    s = str(n)
    length = len(s)

    for sub_len in range(1, length):
        if length % sub_len != 0:
            continue
        repeat_count = length // sub_len
        if repeat_count < 2:
            continue
        part = s[:sub_len]
        if part * repeat_count == s:
            return True

    return False


def sum_invalid_ids(line: str) -> int:
    total = 0
    for part in line.strip().split(","):
        part = part.strip()
        if not part:
            continue
        start_str, end_str = part.split("-")
        start = int(start_str)
        end = int(end_str)
        for n in range(start, end + 1):
            if is_invalid_id(n):
                total += n
    return total

with open("src/day 2/data/day2.txt") as f:
    line = f.read().strip()
print(sum_invalid_ids(line))
