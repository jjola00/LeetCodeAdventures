"Time: O(n), Space: O(n)"
def alternate(s):
    unique_chars = set(s)
    max_len = 0
    
    # Try every pair of distinct characters
    for c1 in unique_chars:
        for c2 in unique_chars:
            if c1 >= c2:  # avoid repeats like (a,b) and (b,a)
                continue
            
            # Filter string to only c1 and c2
            filtered = [ch for ch in s if ch == c1 or ch == c2]
            
            # Check if alternating
            valid = True
            for i in range(1, len(filtered)):
                if filtered[i] == filtered[i-1]:
                    valid = False
                    break
            
            if valid:
                max_len = max(max_len, len(filtered))
    
    return max_len