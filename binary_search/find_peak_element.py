
from typing import List, Optional

def find_peak_element(nums: List[int]) -> Optional[int]:
    """Return index of a peak element (nums[i] > neighbors). Assumes nums non-empty.
    Uses binary search comparing mid and mid+1.
    Time: O(log n), Space: O(1)
    """
    n = len(nums)
    if n == 0:
        return None
    if n == 1:
        return 0
    left, right = 0, n - 1
    while left < right:
        mid = (left + right) // 2
        # Compare mid with next element; move towards the slope up
        if nums[mid] > nums[mid + 1]:
            right = mid
        else:
            left = mid + 1
    return left
