
from typing import List

def binary_search(arr: List[int], target: int) -> int:
    """Return index of target in sorted arr, else -1.
    Time: O(log n), Space: O(1)
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
