
def staircase(n: int) -> None:
    """Print right-aligned staircase of height n."""
    for i in range(1, n + 1):
        spaces = ' ' * (n - i)
        hashes = '#' * i
        print(spaces + hashes)
