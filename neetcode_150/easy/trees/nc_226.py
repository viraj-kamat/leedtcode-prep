# https://leetcode.com/problems/invert-binary-tree/
# https://www.youtube.com/watch?v=OnSn2XEQ4MY


def invertTree(root):
    if not root:
        return root

    stack = [root]
    while stack:
        element = stack.pop()
        left, right = element.left, element.right
        element.left, element.right = right, left
        if right:
            stack.append(right)
        if left:
            stack.append(left)

    return root


"""
        1
      /   \
     2     3
    / \   / \
   4   5 6   7

        1
      /   \
     2     3
    /     /
   4     7

"""


# Test cases
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def tree_to_list(root):
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node is None:
            result.append(None)
            continue
        result.append(node.val)
        queue.append(node.left)
        queue.append(node.right)
    while result and result[-1] is None:
        result.pop()
    return result


# Example 1: [4,2,7,1,3,6,9] -> [4,7,2,9,6,3,1]
tree1 = TreeNode(4)
tree1.left = TreeNode(2)
tree1.right = TreeNode(7)
tree1.left.left = TreeNode(1)
tree1.left.right = TreeNode(3)
tree1.right.left = TreeNode(6)
tree1.right.right = TreeNode(9)
result1 = invertTree(tree1)
assert tree_to_list(result1) == [4, 7, 2, 9, 6, 3, 1], f"Got {tree_to_list(result1)}"

# Example 2: [2,1,3] -> [2,3,1]
tree2 = TreeNode(2)
tree2.left = TreeNode(1)
tree2.right = TreeNode(3)
result2 = invertTree(tree2)
assert tree_to_list(result2) == [2, 3, 1], f"Got {tree_to_list(result2)}"

# Example 3: [] -> []
assert invertTree(None) is None

# Edge case: Single node
tree4 = TreeNode(1)
result4 = invertTree(tree4)
assert tree_to_list(result4) == [1], f"Got {tree_to_list(result4)}"

# Edge case: Left-skewed tree
tree5 = TreeNode(1)
tree5.left = TreeNode(2)
tree5.left.left = TreeNode(3)
result5 = invertTree(tree5)
assert tree_to_list(result5) == [1, None, 2, None, 3], f"Got {tree_to_list(result5)}"

print("All tests passed!")
