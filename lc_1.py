# https://leetcode.com/problems/two-sum/description/


def twoSum(arr, target):
    balances = {}
    if arr is None or len(arr) == 0:
        return None

    for i, x in enumerate(arr):
        bal = target - x
        if bal in balances:
            return [balances[bal], i]

        balances[x] = i
    return None


assert twoSum([2, 7, 11, 15], 9) == [0, 1]
assert twoSum([3, 2, 4], 6) == [1, 2]
assert twoSum([3, 3], 6) == [0, 1]
assert twoSum([2, 3, 5, 6], 11) == [2, 3]
assert twoSum([1, 2, 3], 7) is None
assert twoSum([], 5) is None
assert twoSum(None, 5) is None

print("all tests passed")
