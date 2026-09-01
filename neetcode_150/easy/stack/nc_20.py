# https://leetcode.com/problems/valid-parentheses/
# https://www.youtube.com/watch?v=WTzjTskDFMg


def validParen(chars):
    stack = []

    closeChars = {
        "}": "{",
        ")": "(",
        "]": "["
    }

    openChars = set(["{","(","["])

    for x in chars:
        if x in openChars:
            stack.append(x)
        elif x in closeChars:
            if stack and stack[-1] == closeChars[x]:
                stack.pop()
            else:
                return False

    return len(stack) == 0


assert validParen("()") == True
assert validParen("()[]{}") == True
assert validParen("(]") == False
assert validParen("([)]") == False
assert validParen("{[]}") == True
assert validParen("") == True
assert validParen("(") == False
assert validParen(")") == False
assert validParen("((") == False
assert validParen("]") == False
print("All tests passed")
