def is_invalid_id(n: int) -> bool:
    s = str(n)
    # It must be exactly two copies of some string,
    # so total length must be even.
    if len(s) % 2 != 0:
        return False
    half = len(s) // 2
    return s[:half] == s[half:]


def sum_invalid_ids(line: str) -> int:
    total = 0
    # input is a single line: "a-b,c-d,..."
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
