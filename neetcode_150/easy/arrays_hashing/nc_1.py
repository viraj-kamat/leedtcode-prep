# https://leetcode.com/problems/two-sum/
# https://www.youtube.com/watch?v=KLlXCFG5TnA


def twoSum(arr, target):
    # x + bal = target
    # target - bal = x
    # check if x in balMap
    balMap = {}
    for i,x in enumerate(arr):
        bal = target - x
        if bal in balMap:
            return [balMap[bal], i]
        balMap[x] = i
    return None


assert twoSum([2, 7, 11, 15], 9) == [0, 1]
assert twoSum([3, 2, 4], 6) == [1, 2]
assert twoSum([3, 3], 6) == [0, 1]
assert twoSum([1, 2], 3) == [0, 1]
assert twoSum([-1, -2, -3, -4, -5], -8) == [2, 4]
assert twoSum([0, 4, 3, 0], 0) == [0, 3]
assert twoSum([5, 1], 6) == [0, 1]
print("All tests passed")
