class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class BinaryTree:
    def __init__(self):
        self.root = None

    def pre_order_traversal(self, node):
        if node is None:
            return
        print(node.data, end=" ")
        self.pre_order_traversal(node.left)
        self.pre_order_traversal(node.right)

    def in_order_traversal(self, node):
        if node is None:
            return
        self.in_order_traversal(node.left)
        print(node.data, end=" ")
        self.in_order_traversal(node.right)

    def post_order_traversal(self, node):
        if node is None:
            return
        self.post_order_traversal(node.left)
        self.post_order_traversal(node.right)
        print(node.data, end=" ")

    def level_order_traversal(self, node):
        if node is None:
            return
        queue = []
        queue.append(node)
        while len(queue) > 0:
            print(queue[0].data, end=" ")
            node = queue.pop(0)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

    def search_binary_tree(self, node, data):
        if node is None or node.data == data:
            return node
        if node.data < data:
            return self.search_binary_tree(node.right, data)
        else:
            return self.search_binary_tree(node.left, data)

    def insert_node_binary_tree(self, node, data):
        if self.root is None:
            self.root = Node(data)
        else:
            if node is None:
                return Node(data)
            if data < node.data:
                node.left = self.insert_node_binary_tree(node.left, data)
            else:
                node.right = self.insert_node_binary_tree(node.right, data)
            return node

    def get_deepest_node(self, node):
        if node is None:
            return None
        queue = []
        queue.append(node)
        while len(queue) > 0:
            node = queue.pop(0)
            if node.right is not None:
                queue.append(node.right)
            if node.left is not None:
                queue.append(node.left)
        return node

    def delete_deepest_node(self, node, deepest_node):
        if node is None:
            return None
        if node == deepest_node:
            return None
        if node.right:
            if node.right == deepest_node:
                node.right = None
                return node
            else:
                node.right = self.delete_deepest_node(node.right, deepest_node)
        if node.left:
            if node.left == deepest_node:
                node.left = None
                return node
            else:
                node.left = self.delete_deepest_node(node.left, deepest_node)
        return node

    def delete_node_binary_tree(self, node, data):
        if node is None:
            return None
        if node.data == data:
            if node.left is None and node.right is None:
                return None
            if node.right is None:
                return node.left
            if node.left is None:
                return node.right
            temp_node = node.right
            while temp_node.left:
                temp_node = temp_node.left
            node.data = temp_node.data
            node.right = self.delete_deepest_node(node.right, temp_node)
            return node
        if data < node.data:
            node.left = self.delete_node_binary_tree(node.left, data)
        else:
            node.right = self.delete_node_binary_tree(node.right, data)
        return node

    def delete_binary_tree(self):
        self.root = None
