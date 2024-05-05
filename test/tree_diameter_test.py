import unittest
from src.tree_diameter import max_diameter, BinaryTree, height


class TestBinaryTreeFunctions(unittest.TestCase):
    def test_height(self):
        root = BinaryTree(1)
        root.left = BinaryTree(3)
        root.left.left = BinaryTree(7)
        root.left.left.left = BinaryTree(8)
        root.left.left.left.left = BinaryTree(9)

        root.right = BinaryTree(2)
        root.left.right = BinaryTree(4)
        root.left.right.right = BinaryTree(5)
        root.left.right.right.right = BinaryTree(6)

        self.assertEqual(height(root), 5)

    def test_max_diameter(self):
        root = BinaryTree(1)
        root.left = BinaryTree(3)
        root.left.left = BinaryTree(7)
        root.left.left.left = BinaryTree(8)
        root.left.left.left.left = BinaryTree(9)

        root.right = BinaryTree(2)
        root.left.right = BinaryTree(4)
        root.left.right.right = BinaryTree(5)
        root.left.right.right.right = BinaryTree(6)
        root.left.right.right.right.right = BinaryTree(10)
        root.left.right.right.right.right.right = BinaryTree(11)
        root.left.right.right.right.right.right.right = BinaryTree(12)
        root.left.right.right.right.right.right.right.right = BinaryTree(13)

        self.assertEqual(max_diameter(root), 10)


if __name__ == '__main__':
    unittest.main()
