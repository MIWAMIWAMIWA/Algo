class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def is_balanced(root):
    if root is None or count_nodes(root) == -1:
        return False
    else:
        return True


def count_nodes(node):
    if node.left is None:
        left_count = 0
    else:
        left_count = count_nodes(node.left)
    if node.right is None:
        right_count = 0
    else:
        right_count = count_nodes(node.right)
    if left_count == -1 or right_count == -1 or abs(left_count - right_count) > 1:
        return -1
    else:
        return max(right_count, left_count) + 1


