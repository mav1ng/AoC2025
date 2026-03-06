import sys
import os

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from aoc_helpers.input_utils import read_input_lines

def solve_day1_part1():
    """Solves the Day 1, Part One puzzle."""
    rotations = read_input_lines('day1/input.txt')

    current_position = 50   # start halfway round the 100-step circular dial
    zero_count = 0

    for rotation in rotations:
        if not rotation:
            continue

        direction = rotation[0]         # 'R' or 'L'
        distance = int(rotation[1:])    # number of steps to move

        if direction == 'R':
            current_position = (current_position + distance) % 100   # wrap clockwise
        elif direction == 'L':
            current_position = (current_position - distance) % 100   # wrap anti-clockwise

        # Count only exact landings on position 0 (not pass-throughs)
        if current_position == 0:
            zero_count += 1

    return zero_count

def solve_day1_part2():
    """Solves the Day 1, Part Two puzzle."""
    rotations = read_input_lines('day1/input.txt')

    current_position = 50   # same starting position as Part 1
    zero_count = 0

    for rotation in rotations:
        if not rotation:
            continue

        direction = rotation[0]
        distance = int(rotation[1:])

        if direction == 'R':
            # Every full lap of 100 steps crosses position 0 once;
            # integer division gives the number of crossings cleanly.
            zero_count += (current_position + distance) // 100
            current_position = (current_position + distance) % 100
        elif direction == 'L':
            # For left turns we step one click at a time so that every
            # individual crossing of 0 is counted (avoids off-by-one).
            for _ in range(distance):
                current_position -= 1
                if current_position == -1:   # underflow → wrap to top of dial
                    current_position = 99
                if current_position == 0:
                    zero_count += 1

    return zero_count

if __name__ == '__main__':
    password_one = solve_day1_part1()
    print(f"Part One Password: {password_one}")
    password_two = solve_day1_part2()
    print(f"Part Two Password: {password_two}")