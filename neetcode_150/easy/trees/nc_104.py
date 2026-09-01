# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# https://www.youtube.com/watch?v=hTM3phVI6YQ

def maxDepth(root):
    if not root:
        return 0
    else:
        return 1 + max(maxDepth(root.left), maxDepth(root.right))


# Test cases
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Example 1: [3,9,20,null,null,15,7]
#       3
#      / \
#     9  20
#       /  \
#      15   7
tree1 = TreeNode(3)
tree1.left = TreeNode(9)
tree1.right = TreeNode(20)
tree1.right.left = TreeNode(15)
tree1.right.right = TreeNode(7)
assert maxDepth(tree1) == 3, f"Expected 3, got {maxDepth(tree1)}"

# Example 2: [2,null,3]
#     2
#      \
#       3
tree2 = TreeNode(2)
tree2.right = TreeNode(3)
assert maxDepth(tree2) == 2, f"Expected 2, got {maxDepth(tree2)}"

# Edge case: Single node
tree3 = TreeNode(1)
assert maxDepth(tree3) == 1, f"Expected 1, got {maxDepth(tree3)}"

# Edge case: Empty tree (None)
tree4 = None
assert maxDepth(tree4) == 0, f"Expected 0, got {maxDepth(tree4)}"

# Edge case: Linear tree (left-skewed)
#     1
#    /
#   2
#  /
# 3
tree5 = TreeNode(1)
tree5.left = TreeNode(2)
tree5.left.left = TreeNode(3)
assert maxDepth(tree5) == 3, f"Expected 3, got {maxDepth(tree5)}"

# Edge case: Linear tree (right-skewed)
#     1
#      \
#       2
#        \
#         3
tree6 = TreeNode(1)
tree6.right = TreeNode(2)
tree6.right.right = TreeNode(3)
assert maxDepth(tree6) == 3, f"Expected 3, got {maxDepth(tree6)}"

print("All tests passed!")
