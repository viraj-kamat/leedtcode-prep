# https://leetcode.com/problems/merge-two-sorted-lists/
# https://www.youtube.com/watch?v=XIdigk956u0


class ListNode():
    def __init__(self, val=None, next=None) -> None:
        self.val = val
        self.next = next

def mergeLists(l1,l2):
    dummy = ListNode(None,None)
    head = dummy



    while l1 and l2:
        if l1.val <= l2.val:
            dummy.next = l1
            l1 = l1.next
        else:
            dummy.next = l2
            l2 = l2.next
        dummy = dummy.next

    if l1 or l2:
        dummy.next = l1 or l2
    return head.next


def build(values):
    dummy = ListNode()
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def to_list(node):
    out = []
    while node:
        out.append(node.val)
        node = node.next
    return out


assert to_list(mergeLists(build([1, 2, 4]), build([1, 3, 4]))) == [1, 1, 2, 3, 4, 4]
assert to_list(mergeLists(build([]), build([]))) == []
assert to_list(mergeLists(build([]), build([0]))) == [0]
assert to_list(mergeLists(build([5]), build([1]))) == [1, 5]
assert to_list(mergeLists(build([1, 2, 3]), build([4, 5, 6]))) == [1, 2, 3, 4, 5, 6]
assert to_list(mergeLists(build([4, 5, 6]), build([1, 2, 3]))) == [1, 2, 3, 4, 5, 6]
assert to_list(mergeLists(build([1, 1, 1]), build([1, 1]))) == [1, 1, 1, 1, 1]

print("All tests passed.")
