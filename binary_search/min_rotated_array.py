
from typing import List

def find_min(nums: List[int]) -> int:
    """Minimum in rotated sorted array (no duplicates).
    Time: O(log n), Space: O(1)
    """
    if not nums:
        raise ValueError("nums must be non-empty")
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]
