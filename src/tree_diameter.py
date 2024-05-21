class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def height(node):
    if not node:
        return 0
    return 1 + max(height(node.left), height(node.right))


def max_diameter(node):
    if node is None:
        return 0

    l_height = height(node.left)
    r_height = height(node.right)

    l_diameter = max_diameter(node.left)
    r_diameter = max_diameter(node.right)

    max_diam = max(l_diameter, r_diameter, l_height + r_height)

    return max_diam
