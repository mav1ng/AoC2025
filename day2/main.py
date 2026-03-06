import sys
import os

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from aoc_helpers.input_utils import read_input_single_line

def is_invalid_id_part_one(n):
    """Checks if an ID is invalid for Part One (repeated twice)."""
    s = str(n)
    length = len(s)

    # An odd-length number can never be split into two equal halves
    if length % 2 != 0:
        return False

    half_length = length // 2
    first_half  = s[:half_length]
    second_half = s[half_length:]

    # Invalid ↔ the number is literally its own first half written twice
    return first_half == second_half

def is_invalid_id_part_two(n):
    """Checks if an ID is invalid for Part Two (repeated at least twice)."""
    s = str(n)
    length = len(s)

    # Try every candidate pattern length from 1 up to half the total length.
    # A pattern of length i is only viable if it divides the total length evenly.
    for i in range(1, length // 2 + 1):
        if length % i == 0:
            pattern = s[:i]
            num_repeats = length // i
            # Reconstruct the full string by tiling the pattern; if it matches
            # the original, the number is a repetition of that pattern.
            if pattern * num_repeats == s:
                return True
    return False

def solve_part_one():
    """Solves the Day 2, Part One puzzle."""
    input_data = read_input_single_line('day2/input.txt')
    total_sum = 0
    if not input_data: return 0

    range_strings = [r for r in input_data.split(',') if r]
    for range_str in range_strings:
        try:
            start_str, end_str = range_str.split('-')
            start, end = int(start_str), int(end_str)
            for i in range(start, end + 1):
                if is_invalid_id_part_one(i):
                    total_sum += i
        except ValueError:
            print(f"Skipping malformed range: {range_str}")
            continue
    return total_sum

def solve_part_two():
    """Solves the Day 2, Part Two puzzle."""
    input_data = read_input_single_line('day2/input.txt')
    total_sum = 0
    if not input_data: return 0

    range_strings = [r for r in input_data.split(',') if r]
    for range_str in range_strings:
        try:
            start_str, end_str = range_str.split('-')
            start, end = int(start_str), int(end_str)
            for i in range(start, end + 1):
                if is_invalid_id_part_two(i):
                    total_sum += i
        except ValueError:
            print(f"Skipping malformed range: {range_str}")
            continue
    return total_sum

if __name__ == '__main__':
    part_one_sum = solve_part_one()
    print(f"Part One: The sum of all invalid IDs is: {part_one_sum}")
    
    part_two_sum = solve_part_two()
    print(f"Part Two: The sum of all invalid IDs is: {part_two_sum}")