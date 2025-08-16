
from typing import List

def plus_minus(arr: List[int]) -> None:
    """Print ratios of positives, negatives, and zeros to 6 decimals."""
    n = len(arr)
    if n == 0:
        print(f"{0.0:.6f}\n{0.0:.6f}\n{0.0:.6f}")
        return
    pos = sum(1 for x in arr if x > 0)
    neg = sum(1 for x in arr if x < 0)
    zer = n - pos - neg
    print(f"{pos/n:.6f}")
    print(f"{neg/n:.6f}")
    print(f"{zer/n:.6f}")
