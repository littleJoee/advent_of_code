from functools import cache

with open('2025/day-7/input.txt') as f:
    grid = [list(line.strip()) for line in f.read().split()]

s = [(r, c) for r, row in enumerate(grid) for c, char in enumerate(row) if char == 'S'][0]
@cache
def solve(r, c):
    if r > len(grid) - 1: return 1

    if grid[r][c] == '.' or grid[r][c] == 'S':
        return solve(r + 1, c)
    elif grid[r][c] == '^':
        return solve(r, c - 1) + solve(r, c + 1)

print(solve(*s))