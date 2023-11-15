import unittest
from src.is_balanced import BinaryTree
from src.is_balanced import is_balanced


class MyTestCase(unittest.TestCase):
    def test_default_value(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.right = BinaryTree(3)
        root.left.left = BinaryTree(4)
        root.left.right = BinaryTree(5)
        self.assertEqual(True, is_balanced(root))

    def test_falsecase_value(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.right = BinaryTree(3)
        root.left.left = BinaryTree(4)
        root.left.right = BinaryTree(5)
        root.left.left.left = BinaryTree(7)
        self.assertEqual(False, is_balanced(root))

    def test_bigger_tree(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.right = BinaryTree(3)
        root.left.left = BinaryTree(4)
        root.left.right = BinaryTree(5)
        root.right.left = BinaryTree(6)
        root.right.right = BinaryTree(7)
        root.left.left.left = BinaryTree(8)
        root.right.right.right = BinaryTree(9)
        self.assertEqual(True, is_balanced(root))

    def test_none_value(self):
        self.assertEqual(False, is_balanced(None))


if __name__ == '__main__':
    unittest.main()
