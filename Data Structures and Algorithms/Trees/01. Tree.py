class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Tree:
    def __init__(self, root=None):
        self.root = root

    def add_node(self, value, parent_value):
        parent = self._find_node(parent_value, self.root)
        if parent:
            if parent.left is None:
                parent.left = TreeNode(value)
            elif parent.right is None:
                parent.right = TreeNode(value)
        else:
            if self.root is None:
                self.root = TreeNode(value)

    def _find_node(self, value, node):
        if node is None:
            return None
        if node.value == value:
            return node
        left = self._find_node(value, node.left)
        if left:
            return left
        right = self._find_node(value, node.right)
        if right:
            return right
        return None


tree = Tree()
tree.add_node(3, None)
tree.add_node(4, 3)
tree.add_node(5, 3)
tree.add_node(6, 4)
