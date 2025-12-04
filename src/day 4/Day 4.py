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
        r, c = row + dr, col + dc
        if 0 <= r < len(grid) and 0 <= c < len(grid[r]) and grid[r][c] == '@':
            neighbors += 1
            if neighbors >= 4:
                return False
    return True


def solve(data: list[str]) -> int:
    grid = parse_grid(data)
    total = 0
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell == '@' and is_accessible(grid, r, c):
                total += 1
    return total


if __name__ == '__main__':
    print(solve(load_input()))
