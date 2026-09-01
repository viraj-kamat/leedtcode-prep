# https://leetcode.com/problems/min-cost-climbing-stairs/
# https://www.youtube.com/watch?v=ktmzAZWkEZ0


def minCostStairs(arr):

    length = len(arr)

    if length <= 2:
        return min(arr) or 0

    finalArr = [0]*(length+1)

    finalArr[0], finalArr[1] = arr[0], arr[1]

    for i in range(2,length+1):

        if i == length:
            curCost = 0
        else:
            curCost = arr[i]

        minCurCost = min(finalArr[i-1],finalArr[i-2])
        finalArr[i] = curCost + minCurCost
    return finalArr[-1]


if __name__ == "__main__":
    assert minCostStairs([10,15,20]) == 15
    assert minCostStairs([1,100,1,1,1,100,1,1,100,1]) == 6
    assert minCostStairs([1,2]) == 1
    assert minCostStairs([0,0]) == 0
    assert minCostStairs([0,1,2,2]) == 2
    assert minCostStairs([10,5]) == 5
    print("All tests passed")
