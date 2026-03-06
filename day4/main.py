import sys
import os

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from aoc_helpers.input_utils import read_input_lines

def count_neighbors(grid, r, c, rows, cols):
    """Counts the number of adjacent '@' rolls for a given cell."""
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),          (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]
    neighbor_count = 0
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '@':
            neighbor_count += 1
    return neighbor_count

def solve_part_one():
    """Solves Day 4, Part One."""
    grid = read_input_lines('day4/input.txt')
    if not grid: return 0

    rows, cols = len(grid), len(grid[0])
    accessible_rolls_count = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '@':
                if count_neighbors(grid, r, c, rows, cols) < 4:
                    accessible_rolls_count += 1
    return accessible_rolls_count

def solve_part_two():
    """Solves Day 4, Part Two using iterative removal."""
    grid_str = read_input_lines('day4/input.txt')
    if not grid_str: return 0

    # Convert to a mutable 2-D list so we can overwrite cells in-place
    grid = [list(row) for row in grid_str]
    rows, cols = len(grid), len(grid[0])
    total_removed_count = 0

    while True:
        # --- snapshot phase ---
        # Collect every roll that qualifies for removal *before* removing any.
        # This mirrors a simultaneous-update rule (similar to Conway's Game of
        # Life): neighbour counts must be based on the state at the start of
        # the round, not on partially-updated state.
        rolls_to_remove = [
            (r, c)
            for r in range(rows)
            for c in range(cols)
            if grid[r][c] == '@' and count_neighbors(grid, r, c, rows, cols) < 4
        ]

        if not rolls_to_remove:
            break   # grid has stabilised — no qualifying rolls remain

        # --- removal phase ---
        total_removed_count += len(rolls_to_remove)
        for r, c in rolls_to_remove:
            grid[r][c] = '.'   # erase the roll; '.' denotes an empty cell

    return total_removed_count

if __name__ == '__main__':
    part_one_count = solve_part_one()
    print(f"Part One: The number of accessible rolls is: {part_one_count}")

    part_two_count = solve_part_two()
    print(f"Part Two: The total number of removable rolls is: {part_two_count}")