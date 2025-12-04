from pathlib import Path

ADJACENT = (
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1),
)


def load_input() -> list[str]:
    input_path = Path('src/day 4/data/day4.txt')
    return input_path.read_text().splitlines()


def parse_grid(data: list[str]) -> list[list[str]]:
    return [list(line.strip()) for line in data if line.strip()]


def is_accessible(grid: list[list[str]], row: int, col: int) -> bool:
    neighbors = 0
    for dr, dc in ADJACENT:
        rr, cc = row + dr, col + dc
        if 0 <= rr < len(grid) and 0 <= cc < len(grid[rr]) and grid[rr][cc] == '@':
            neighbors += 1
            if neighbors >= 4:
                return False
    return True


def solve(data: list[str]) -> int:
    grid = parse_grid(data)
    total_removed = 0

    while True:
        removable: list[tuple[int, int]] = []
        for r, row in enumerate(grid):
            for c, cell in enumerate(row):
                if cell == '@' and is_accessible(grid, r, c):
                    removable.append((r, c))

        if not removable:
            break

        for r, c in removable:
            grid[r][c] = '.'
        total_removed += len(removable)

    return total_removed


if __name__ == '__main__':
    print(solve(load_input()))
