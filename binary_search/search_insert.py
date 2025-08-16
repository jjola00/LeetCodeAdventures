
from typing import List

def search_insert(nums: List[int], target: int) -> int:
    """Return index if found; else insertion index in sorted nums.
    Time: O(log n), Space: O(1)
    """
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left
