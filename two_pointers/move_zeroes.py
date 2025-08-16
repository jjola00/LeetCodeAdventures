
from typing import List

def move_zeroes(nums: List[int]) -> None:
    """Move all zeros to the end while keeping order of non-zeros (in-place).
    Time: O(n), Space: O(1)
    """
    insert = 0
    for x in nums:
        if x != 0:
            nums[insert] = x
            insert += 1
    # fill the rest with zeros
    for i in range(insert, len(nums)):
        nums[i] = 0
