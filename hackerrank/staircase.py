
def staircase(n: int) -> None:
    """Print right-aligned staircase of height n.
    Time: O(n^2), Space: O(n)
    """
    for i in range(1, n + 1):
        spaces = ' ' * (n - i)
        hashes = '#' * i
        print(spaces + hashes)
