# https://leetcode.com/problems/climbing-stairs/
# https://www.youtube.com/watch?v=Y0lT9Fck7qI


def climbStairs(n):
    if n == 1 or n == 2:
       return n

    n = n+1

    arr = [0]*n
    arr[-1], arr[-2] = 1, 1

    for stp in range(n-3,-1,-1):
        curStps = arr[stp+1] + arr[stp+2]
        arr[stp] = curStps
    return arr[0]


if __name__ == "__main__":
    assert climbStairs(1) == 1
    assert climbStairs(2) == 2
    assert climbStairs(3) == 3
    assert climbStairs(4) == 5
    assert climbStairs(5) == 8
    assert climbStairs(6) == 13
    assert climbStairs(10) == 89
    assert climbStairs(20) == 10946
    print("All tests passed")
