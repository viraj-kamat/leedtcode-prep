# https://leetcode.com/problems/kth-largest-element-in-a-stream/
# https://www.youtube.com/watch?v=hOjcdrqMoQ8

import heapq
class KthLargest:


    def __init__(self, k: int, nums: List[int]):
        count = len(nums)
        heapq.heapify(nums)
        self.nums = nums
        while count > k:
            heapq.heappop(self.nums)
            count -= 1
        self.count = count
        self.k = k

    def add(self, val: int) -> int:

        heapq.heappush(self.nums, val)
        self.count += 1
        if self.count > self.k:
            heapq.heappop(self.nums)
            self.count -=1
        return self.nums[0]




# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

if __name__ == "__main__":
    kl = KthLargest(3, [4, 5, 8, 2])
    assert kl.add(3) == 4
    assert kl.add(5) == 5
    assert kl.add(10) == 5
    assert kl.add(9) == 8
    assert kl.add(4) == 8

    kl2 = KthLargest(1, [])
    assert kl2.add(-3) == -3
    assert kl2.add(-2) == -2
    assert kl2.add(-4) == -2
    assert kl2.add(0) == 0
    assert kl2.add(4) == 4

    kl3 = KthLargest(2, [0])
    assert kl3.add(-1) == -1
    assert kl3.add(1) == 0
    assert kl3.add(-2) == 0
    assert kl3.add(-4) == 0
    assert kl3.add(3) == 1

    print("All tests passed")

"""
Time complexity:

__init__(k, nums), where n = len(nums):
  1. nums = [x for x in nums]        -> O(n), copy the list.
  2. heapq.heapify(nums)             -> O(n), heapify is linear, not n log n.
     Even though it looks like it should be O(n log n) (n elements, each
     seemingly needing a log n "sift"), the classic proof sums sift-down
     costs level by level: most nodes are near the bottom of the tree and
     need almost no work, and that geometric sum collapses to O(n) total.
  3. while count > k: heappop        -> runs (n - k) times, once per
     excess element that needs to be trimmed off the heap.
     3a. each heappop                -> O(log n) per call in the worst
         case (heap size is at most n while this loop runs, and popping
         means removing the root then sifting the last element down,
         which costs at most the height of the heap, log n).
     3b. total for the loop          -> O((n - k) log n), i.e. number of
         pops times cost per pop.
  4. combine steps 1-3               -> O(n) + O(n) + O((n - k) log n)
                                         = O(n log n) worst case overall
     (the heapify is dominated once you also pay for repeated pops down
     to k elements; if n and k are close, the pop loop barely runs, but
     the bound is still expressed against n in the worst case).

add(val):
  1. heapq.heappush(self.nums, val)  -> O(log k), because self.nums is
     always kept at size <= k by the trimming logic, so pushing one more
     element and sifting it up costs at most the height of a heap of
     size k+1, which is O(log k).
  2. if self.count > self.k: heappop -> O(log k) when it fires, for the
     same reason: the heap never grows past ~k+1 elements before this
     pop brings it back down, so the sift-down after removing the root
     is bounded by O(log k).
  3. combine steps 1-2               -> O(log k) per call, since both the
     push and the conditional pop are each O(log k) and they happen at
     most once per add.

Space complexity:
  1. self.nums after trimming        -> O(k), holds at most k elements
     at any point after __init__ finishes and between add calls.
  2. temporary list in step 1 of
     __init__ before trimming        -> O(n), the full copy of nums that
     exists briefly before the while loop shrinks it down to k elements;
     this is transient, not part of the steady-state footprint.
  3. steady-state space               -> O(k), since the only long-lived
     state the object keeps is the size-k heap plus a couple of ints
     (self.count, self.k).
"""
