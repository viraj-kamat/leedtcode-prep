# https://leetcode.com/problems/valid-parentheses/description/


def validate(chars: str):

    if chars == "":
        return True

    if chars.strip() == "":
        return False


    hMap: dict[str,str] = {
        ")":"(",
        "]":"[",
        "}":"{"
    }

    openChars = set(["(","{","["])

    stack: list[str] = []


    for x in chars:
        if x in openChars:
            stack.append(x)
        elif x in hMap:
            if stack and hMap[x] == stack[-1]:
                stack.pop()
            else:
                return False
        else:
            return False

    else:
        return len(stack) == 0


# Official examples
assert validate("()") == True
assert validate("()[]{}" ) == True
assert validate("(") == False
assert validate("([)]") == False
assert validate("{[]}") == True

# Edge cases
assert validate("") == True
assert validate(")") == False
assert validate("(((") == False
assert validate(")))") == False
assert validate("([{}])") == True
assert validate("[({})]") == True
assert validate("([]") == False
assert validate("[)") == False

print("all tests passed")
