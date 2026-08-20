# https://leetcode.com/problems/valid-palindrome/description/



def check_palindrom(chars):
    length = len(chars)
    if length == 0:
        return True

    left, right = 0, length-1

    while left <= right:

        if not chars[left].isalnum():
            left += 1
            continue
        if not chars[right].isalnum():
            right -= 1
            continue

        if chars[left].lower() != chars[right].lower():
            return False

        left += 1
        right -= 1

    return True


if __name__ == "__main__":
    assert check_palindrom("A man, a plan, a canal: Panama") is True
    assert check_palindrom("race a car") is False
    assert check_palindrom(" ") is True
    assert check_palindrom("") is True
    assert check_palindrom("a") is True
    assert check_palindrom(".,") is True
    assert check_palindrom("0P") is False
    assert check_palindrom("ab_a") is True
    assert check_palindrom("12321") is True
    assert check_palindrom("1a2") is False
    print("All tests passed.")
