
def length_of_longest_substring(s: str) -> int:
    """Sliding window with set.
    Time: O(n), Space: O(min(n, Σ))
    """
    seen = set()
    left = 0
    max_len = 0
    for right, ch in enumerate(s):
        while ch in seen:
            seen.remove(s[left])
            left += 1
        seen.add(ch)
        max_len = max(max_len, right - left + 1)
    return max_len
