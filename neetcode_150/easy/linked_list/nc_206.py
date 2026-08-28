# https://leetcode.com/problems/reverse-linked-list/
# https://www.youtube.com/watch?v=G0_I-ZF0S38


class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head):

    if not head:
        return None

    prev = None
    cur = head
    while cur.next:
        tmp = cur.next
        cur.next = prev
        prev, cur = cur, tmp
    else:
        cur.next = prev
    return cur    

        
    
    # prev = None
    # cur = head
    # while cur:
    #     tmp = cur.next
    #     cur.next = prev
    #     prev, cur = cur, tmp
    # return prev



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


assert to_list(reverseList(build([1, 2, 3, 4, 5]))) == [5, 4, 3, 2, 1]
assert to_list(reverseList(build([1, 2]))) == [2, 1]
assert to_list(reverseList(build([1]))) == [1]
assert to_list(reverseList(build([]))) == []
print("All tests passed")
