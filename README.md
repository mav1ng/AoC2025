# 🎄 Advent of Code 2025

My solutions to the [Advent of Code 2025](https://adventofcode.com/2025) puzzles, written in **Python 3**.

---

## Progress

| Day | Puzzle Theme | Part 1 | Part 2 |
|:---:|---|:---:|:---:|
| [Day 1](day1/main.py) | Circular Track Navigation | ⭐ | ⭐ |
| [Day 2](day2/main.py) | Repeated ID Validation | ⭐ | ⭐ |
| [Day 3](day3/main.py) | Battery Bank Joltage | ⭐ | ⭐ |
| [Day 4](day4/main.py) | Roll Grid Removal | ⭐ | ⭐ |

**Total stars: 8 ⭐**

---

## Repository Structure

```
AoC2025/
├── aoc_helpers/          # Shared input-parsing utilities
│   └── input_utils.py
├── day1/
│   ├── main.py           # Solution
│   └── input.txt         # Puzzle input (personal — not redistributed)
├── day2/
│   ├── main.py
│   └── input.txt
├── day3/
│   ├── main.py
│   └── input.txt
└── day4/
    ├── main.py
    └── input.txt
```

---

## Design Decisions

- **Shared utilities** — `aoc_helpers/input_utils.py` centralises all file I/O so each solution stays focused on puzzle logic.
- **Consistent structure** — every `main.py` exposes `solve_part_one()` and `solve_part_two()` functions, making it easy to import or test individual parts.
- **Self-contained days** — each solution can be run directly from the project root without any external dependencies.

---

## Running a Solution

All scripts must be run from the **project root** so that relative input paths resolve correctly:

```bash
# Run a specific day
python day1/main.py

# Run all days sequentially
for d in 1 2 3 4; do python day$d/main.py; done
```

> **Note:** Puzzle inputs are personal to each participant. Per the [AoC guidelines](https://adventofcode.com/about), they are not redistributed here. Place your own `input.txt` in the relevant day folder before running.

---

## Requirements

- Python 3.8+
- No third-party libraries — standard library only.
