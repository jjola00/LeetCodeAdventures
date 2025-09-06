def max_sum_subarray(nums, k):
    # Step 1: build the first window
    window_sum = sum(nums[:k])
    max_sum = window_sum
    
    # Step 2: slide the window
    for i in range(k, len(nums)):
        # remove the element going out (nums[i-k])
        # add the new element coming in (nums[i])
        window_sum += nums[i] - nums[i-k]
        max_sum = max(max_sum, window_sum)
    
    return max_sum

print(max_sum_subarray([1, 3, 2, 5, 1, 1, 2, 3], 3))  # 10 (from [3,2,5])

def lengthOfLongestSubstring(s: str) -> int:
    seen = set()   # chars in current window
    left = 0       # window start
    max_len = 0

    for right in range(len(s)):
        # if duplicate, shrink window from the left
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        
        # expand window
        seen.add(s[right])
        max_len = max(max_len, right - left + 1)
    
    return max_len

print(lengthOfLongestSubstring("abcabcbb"))  # 3 ("abc")
print(lengthOfLongestSubstring("bbbbb"))     # 1 ("b")
print(lengthOfLongestSubstring("pwwkew"))    # 3 ("wke")
