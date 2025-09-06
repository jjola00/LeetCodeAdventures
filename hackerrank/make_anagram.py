"Time: O(n^2), Space: O(n)"
def makeAnagram(a, b):
    set1 = list(a)
    count = 0
    i = 0
    j = 0
    
    while i < len(b):
        if b[i] not in set1:
            count +=1
            b = b[:i] + b[i+1:]
        else:
            if set1.count(b[i]) > 1:
                set1.remove(b[i])
                count += 1
                i += 1
            i += 1
    set2 = list(b)
    a = ''.join(set1)
    while j < len(a):
        if a[j] not in set2:
            count += 1
            a = a[:j] + a[j+1:]
        else:
            if set2.count(a[j]) > 1:
                set2.remove(a[j])
                count += 1
                j += 1
            j += 1
    return count

    from collections import Counter

def makeAnagram(a, b):
    freq_a = Counter(a)
    freq_b = Counter(b)
    deletions = 0
    
    for ch in set(freq_a.keys()).union(set(freq_b.keys())):
        deletions += abs(freq_a.get(ch, 0) - freq_b.get(ch, 0))
    
    return deletions
"Time: O(n), Space: O(1)"