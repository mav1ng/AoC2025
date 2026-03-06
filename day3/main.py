import sys
import os

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from aoc_helpers.input_utils import read_input_lines

def find_max_joltage_part_one(bank):
    """Finds the largest two-digit number that can be formed from a bank of batteries."""
    max_joltage = 0
    n = len(bank)
    if n < 2:
        return 0

    # Brute-force all ordered pairs (i, j) — O(n²) but n is small per line
    for i in range(n):
        for j in range(i + 1, n):
            current_joltage = int(bank[i] + bank[j])   # concatenate, not add
            if current_joltage > max_joltage:
                max_joltage = current_joltage

    return max_joltage

def find_max_joltage_part_two(bank):
    """Finds the largest 12-digit number using a greedy approach."""
    k = 12   # target output length
    n = len(bank)
    if n < k:
        return 0

    result = []
    current_pos = 0
    for i in range(k, 0, -1):
        # We still need to pick (i) digits after this one.
        # The latest index we can choose for the current digit is n - i,
        # leaving at least (i-1) characters to fill the remaining slots.
        search_end = n - i + 1
        best_digit = '-1'   # sentinel: any real digit ('0'–'9') beats this
        best_pos = -1

        # Scan the allowed window and keep the largest digit seen
        for j in range(current_pos, search_end):
            if bank[j] > best_digit:   # character comparison works for '0'–'9'
                best_digit = bank[j]
                best_pos = j

        result.append(best_digit)
        current_pos = best_pos + 1   # next digit must come after the chosen one

    return int("".join(result))

def solve_part_one():
    """Solves the Day 3, Part One puzzle."""
    banks = read_input_lines('day3/input.txt')
    total_joltage = 0
    for bank in banks:
        if bank:
            total_joltage += find_max_joltage_part_one(bank)
    return total_joltage

def solve_part_two():
    """Solves the Day 3, Part Two puzzle."""
    banks = read_input_lines('day3/input.txt')
    total_joltage = 0
    for bank in banks:
        if bank:
            total_joltage += find_max_joltage_part_two(bank)
    return total_joltage

if __name__ == '__main__':
    part_one_joltage = solve_part_one()
    print(f"Part One: The total output joltage is: {part_one_joltage}")

    part_two_joltage = solve_part_two()
    print(f"Part Two: The total output joltage is: {part_two_joltage}")