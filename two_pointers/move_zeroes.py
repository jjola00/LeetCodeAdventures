



























from typing import List

def move_zeroes(nums: List[int]) -> None:
    """Move all zeros to the end while keeping order of non-zeros (in-place).
    Time: O(n), Space: O(1)
    """
    i, j = 0
    while( j < len(nums - 1)):
        i += 1
        j += 1
        if (i == 0 and j != 0):
            nums[i], nums[j] = nums[j], nums[i]
        if i and j == 0:
            j += 1
        


