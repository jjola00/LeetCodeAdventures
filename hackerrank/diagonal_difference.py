
from typing import List

def diagonal_difference(arr: List[List[int]]) -> int:
    """Absolute difference of primary and secondary diagonal sums."""
    n = len(arr)
    prim = sum(arr[i][i] for i in range(n))
    sec = sum(arr[i][n - 1 - i] for i in range(n))
    return abs(prim - sec)
