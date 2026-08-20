# https://leetcode.com/problems/reverse-linked-list/description/




def reverseList(head):

    if not head:
        return None

    prev = None
    cur = head

    while cur:
        _cur = cur
        _next = cur.next
        cur.next = prev
        cur, prev = _next, _cur
    else:
        return prev


# Test cases
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_to_array(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


# Empty list
assert reverseList(None) is None

# Single node
single = ListNode(1)
assert list_to_array(reverseList(single)) == [1]

# Two nodes
two = ListNode(1, ListNode(2))
assert list_to_array(reverseList(two)) == [2, 1]

# Example 1: [1,2,3,4,5]
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
assert list_to_array(reverseList(head)) == [5, 4, 3, 2, 1]

# Example 2: [1,2]
head = ListNode(1, ListNode(2))
assert list_to_array(reverseList(head)) == [2, 1]

print("All tests passed!")
