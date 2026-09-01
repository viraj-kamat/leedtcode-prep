# https://leetcode.com/problems/contains-duplicate/
# https://www.youtube.com/watch?v=3OamzN90kPg


def containsDuplicate(nums):
    lookup = set()

    for x in nums:
        if x in lookup:
            return True
        lookup.add(x)
    return False


if __name__ == "__main__":
    assert containsDuplicate([1, 2, 3, 1]) == True
    assert containsDuplicate([1, 2, 3, 4]) == False
    assert containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True
    assert containsDuplicate([]) == False
    assert containsDuplicate([1]) == False
    assert containsDuplicate([1, 1]) == True
    print("All tests passed.")
