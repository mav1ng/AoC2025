def read_input_lines(file_path):
    """Reads lines from a file and returns them as a list of strings."""
    with open(file_path, 'r') as f:
        return [line.strip() for line in f.readlines()]

def read_input_single_line(file_path):
    """Reads the entire content of a file and returns it as a single string."""
    with open(file_path, 'r') as f:
        return f.read().strip()
