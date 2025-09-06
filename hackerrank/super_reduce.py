"Time: O(n), Space: O(n)"
def superReducedString(s):
    stack = []
    for ch in s:
        if stack and stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)
    if len(stack) == 0:
        return "Empty String"
    else:
        return "".join(stack)  