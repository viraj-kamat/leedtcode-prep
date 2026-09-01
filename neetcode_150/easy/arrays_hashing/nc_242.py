# https://leetcode.com/problems/valid-anagram/
# https://www.youtube.com/watch?v=9UtInBqnCgA


def isAnagram(s, t):

    arr = [0]*26

    for x in s:
        idx = ord(x) - ord("a")
        arr[idx] += 1
    for x in t:
        idx = ord(x) - ord("a")
        if arr[idx] == 0:
            return False
        arr[idx] -= 1

    return sum(arr) == 0


assert isAnagram("anagram", "nagaram") == True
assert isAnagram("rat", "car") == False
assert isAnagram("", "") == True
assert isAnagram("a", "a") == True
assert isAnagram("a", "b") == False
assert isAnagram("aab", "ab") == False
assert isAnagram("ab", "aab") == False
print("All tests passed")
