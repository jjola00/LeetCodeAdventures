def repeatedString(s, n):
    if not s:
        return 0
    count = 0
    stringLength = len(s)
    for ch in s:
        if ch == 'a':
            count += 1

    full_repeats = n // stringLength      
    remainder = n % stringLength           

    return count * full_repeats + s[:remainder].count('a')