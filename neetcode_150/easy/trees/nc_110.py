# https://leetcode.com/problems/balanced-binary-tree/
# https://www.youtube.com/watch?v=QfJsau0ItOY

def isBalanced(root):
    def checkBalance(root):

        if not root:
            return 0

        leftDepth = checkBalance(root.left)

        if leftDepth == -1:
            return -1

        rightDepth = checkBalance(root.right)

        if rightDepth == -1:
            return -1

        depth  = abs(leftDepth-rightDepth)

        if depth > 1:
            return -1

        return max(1+leftDepth, 1+rightDepth)

    return checkBalance(root) != -1


# Test cases
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Example 1: [3,9,20,null,null,15,7] -> True
tree1 = TreeNode(3)
tree1.left = TreeNode(9)
tree1.right = TreeNode(20)
tree1.right.left = TreeNode(15)
tree1.right.right = TreeNode(7)
assert isBalanced(tree1) == True, f"Expected True, got {isBalanced(tree1)}"

# Example 2: [1,2,2,3,3,null,null,4,4] -> False
tree2 = TreeNode(1)
tree2.left = TreeNode(2)
tree2.right = TreeNode(2)
tree2.left.left = TreeNode(3)
tree2.left.right = TreeNode(3)
tree2.left.left.left = TreeNode(4)
tree2.left.left.right = TreeNode(4)
assert isBalanced(tree2) == False, f"Expected False, got {isBalanced(tree2)}"

# Example 3: [] -> True
tree3 = None
assert isBalanced(tree3) == True, f"Expected True, got {isBalanced(tree3)}"

# Edge case: Single node
tree4 = TreeNode(1)
assert isBalanced(tree4) == True, f"Expected True, got {isBalanced(tree4)}"

# Edge case: Unbalanced deep left-skewed tree
#     1
#    /
#   2
#  /
# 3
tree5 = TreeNode(1)
tree5.left = TreeNode(2)
tree5.left.left = TreeNode(3)
assert isBalanced(tree5) == False, f"Expected False, got {isBalanced(tree5)}"

# Edge case: Unbalance detected deep in the tree (sentinel must propagate)
#         1
#        / \
#       2   2
#      /
#     3
#    /
#   4
tree6 = TreeNode(1)
tree6.left = TreeNode(2)
tree6.right = TreeNode(2)
tree6.left.left = TreeNode(3)
tree6.left.left.left = TreeNode(4)
assert isBalanced(tree6) == False, f"Expected False, got {isBalanced(tree6)}"

print("All tests passed!")

"""
checkBalance is a post-order traversal (left subtree, then right subtree,
then the node itself) that returns height, or -1 as a sentinel meaning
"already unbalanced somewhere below here". isBalanced just checks whether
the root-level call came back as that sentinel.

Example (balanced):
      3
     / \
    9  20
      /  \
     15   7

Call order and return values, in the order each call actually returns:

1. checkBalance(3) calls checkBalance(9) first (leftDepth), since the left
   child is always evaluated before the right.
2. checkBalance(9): leftDepth = checkBalance(None) = 0,
   rightDepth = checkBalance(None) = 0, depth = 0 -> returns max(1,1) = 1.
   Back in checkBalance(3), leftDepth = 1.
3. checkBalance(3) now calls checkBalance(20) for rightDepth.
4. checkBalance(20) calls checkBalance(15) first (its leftDepth).
5. checkBalance(15): leftDepth = 0, rightDepth = 0, depth = 0 -> returns
   max(1,1) = 1. Back in checkBalance(20), leftDepth = 1.
6. checkBalance(20) calls checkBalance(7) for rightDepth.
7. checkBalance(7): leftDepth = 0, rightDepth = 0, depth = 0 -> returns
   max(1,1) = 1. Back in checkBalance(20), rightDepth = 1.
8. checkBalance(20): depth = |1-1| = 0 -> returns max(2,2) = 2.
   Back in checkBalance(3), rightDepth = 2.
9. checkBalance(3): depth = |1-2| = 1, not > 1 -> returns max(2,3) = 3.
10. isBalanced(tree1) -> checkBalance(3) == 3, 3 != -1 -> True.

Example (unbalanced, sentinel propagation):
      1
     /
    2
   /
  3

1. checkBalance(1) calls checkBalance(2) first (leftDepth).
2. checkBalance(2) calls checkBalance(3) first (its leftDepth).
3. checkBalance(3): leftDepth = checkBalance(None) = 0,
   rightDepth = checkBalance(None) = 0, depth = 0 -> returns max(1,1) = 1.
   Back in checkBalance(2), leftDepth = 1.
4. checkBalance(2) calls checkBalance(None) for rightDepth -> 0.
5. checkBalance(2): depth = |1-0| = 1, not > 1 -> returns max(2,1) = 2.
   Back in checkBalance(1), leftDepth = 2.
6. checkBalance(1) calls checkBalance(None) for rightDepth -> 0.
7. checkBalance(1): depth = |2-0| = 2, which is > 1 -> returns -1
   (the sentinel), instead of a real height.
8. isBalanced(tree5) -> checkBalance(1) == -1, -1 != -1 -> False.

If the -1 sentinel appears further down a larger tree, the leftDepth == -1
or rightDepth == -1 checks make every ancestor call return -1 immediately
without computing depth or recursing into the other subtree, so the
sentinel short-circuits all the way back up to the root.
"""
