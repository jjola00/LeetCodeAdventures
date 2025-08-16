
from typing import List

def reverse_string(s: List[str]) -> None:
    """Reverse list of chars in-place.
    Time: O(n), Space: O(1)
    """
    i, j = 0, len(s) - 1
    while i < j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1
