# https://leetcode.com/problems/merge-two-sorted-lists/description/


class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeSortedLists(l1, l2):
    dummy = ListNode()
    cur = dummy

    while l1 and l2:
        if l1.val <= l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next

    cur.next = l1 or l2
    return dummy.next


def _build(values):
    dummy = ListNode()
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def _to_list(node):
    out = []
    while node:
        out.append(node.val)
        node = node.next
    return out


if __name__ == "__main__":
    # official examples
    assert _to_list(mergeSortedLists(_build([1, 2, 4]), _build([1, 3, 4]))) == [1, 1, 2, 3, 4, 4]
    assert _to_list(mergeSortedLists(_build([]), _build([]))) == []
    assert _to_list(mergeSortedLists(_build([]), _build([0]))) == [0]

    # edge cases
    assert _to_list(mergeSortedLists(_build([1]), _build([]))) == [1]
    assert _to_list(mergeSortedLists(_build([]), _build([1]))) == [1]
    assert _to_list(mergeSortedLists(_build([1]), _build([1]))) == [1, 1]
    assert _to_list(mergeSortedLists(_build([1, 1, 1]), _build([1, 1, 1]))) == [1, 1, 1, 1, 1, 1]
    assert _to_list(mergeSortedLists(_build([5, 6, 7]), _build([1, 2, 3]))) == [1, 2, 3, 5, 6, 7]
    assert _to_list(mergeSortedLists(_build([-3, -1, 4]), _build([-2, 0, 4]))) == [-3, -2, -1, 0, 4, 4]
    assert _to_list(mergeSortedLists(_build([1, 2]), _build([3, 4, 5, 6]))) == [1, 2, 3, 4, 5, 6]

    print("all tests passed")
