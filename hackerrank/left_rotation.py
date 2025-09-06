"Time: O(n), Space: O(n"
def rotateLeft(d, arr):
    d = d % len(arr)
    arr = arr[d:] + arr[:d]
    return arr

"Time: O(n), Space: O(1)"
def rotateLeft(d, arr):
    n = len(arr)
    d %= n  # handle d > n

    def reverse(start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    # Step 1: reverse first d elements
    reverse(0, d - 1)
    # Step 2: reverse remaining elements
    reverse(d, n - 1)
    # Step 3: reverse entire array
    reverse(0, n - 1)

    return arr