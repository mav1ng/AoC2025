"""
aoc_helpers — shared utilities for Advent of Code 2025 solutions.

Re-exports the two core input helpers so callers can use either:
    from aoc_helpers import read_input_lines
    from aoc_helpers.input_utils import read_input_lines
"""

from .input_utils import read_input_lines, read_input_single_line

__all__ = ["read_input_lines", "read_input_single_line"]
