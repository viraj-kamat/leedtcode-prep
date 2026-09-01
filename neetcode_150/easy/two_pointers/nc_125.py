# https://leetcode.com/problems/valid-palindrome/
# https://www.youtube.com/watch?v=jJXJ16kPFWg


def isPalindrome(chars):

    length = len(chars)
    if length == 0:
        return True

    left, right = 0, length-1

    while left < right:
        if not chars[left].isalnum():
            left += 1
            continue
        elif not chars[right].isalnum():
            right -= 1
            continue

        if chars[left].lower() != chars[right].lower():
            return False
        left += 1
        right -= 1
    return True


if __name__ == "__main__":
    assert isPalindrome("A man, a plan, a canal: Panama") is True
    assert isPalindrome("race a car") is False
    assert isPalindrome(" ") is True
    assert isPalindrome("") is True
    assert isPalindrome("a") is True
    assert isPalindrome("0P") is False
    assert isPalindrome(".,") is True
    assert isPalindrome("abca") is False
    print("All tests passed.")
