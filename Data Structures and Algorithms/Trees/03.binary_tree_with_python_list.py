class BinaryTree:
    def __init__(self, size):
        self.tree = size * [None]
        self.last_index = 0
        self.max_size = size

    def insert_node(self, value):
        if self.last_index + 1 == self.max_size:
            return "The binary tree is full"
        self.tree[self.last_index + 1] = value
        self.last_index += 1
        return "The value has been inserted"

    def search_node(self, node_value):
        for i in range(len(self.tree)):
            if self.tree[i] == node_value:
                return "Success"
        return "Not Found"

    def pre_order_traversal(self, index):
        if index > self.last_index:
            return
        print(self.tree[index])
        self.pre_order_traversal(index * 2)
        self.pre_order_traversal(index * 2 + 1)

    def in_order_traversal(self, index):
        if index > self.last_index:
            return
        self.in_order_traversal(index * 2)
        print(self.tree[index])
        self.in_order_traversal(index * 2 + 1)

    def post_order_traversal(self, index):
        if index > self.last_index:
            return
        self.post_order_traversal(index * 2)
        self.post_order_traversal(index * 2 + 1)
        print(self.tree[index])

    def level_order_traversal(self, index):
        for i in range(index, self.last_index + 1):
            print(self.tree[i])

    def delete_node(self, value):
        if self.last_index == 0:
            return "There is no node to delete"
        for i in range(1, self.last_index + 1):
            if self.tree[i] == value:
                self.tree[i] = self.tree[self.last_index]
                self.tree[self.last_index] = None
                self.last_index -= 1
                return "The node has been successfully deleted"

    def delete_tree(self):
        self.tree = None
        return "The binary tree has been successfully deleted"


newBT = BinaryTree(8)

print(newBT.insert_node("Drinks"))
print(newBT.insert_node("Hot"))
print(newBT.insert_node("Cold"))

print(newBT.search_node("Hot"))
print(newBT.search_node("Warm"))

print("Pre-Order Traversal:")
newBT.pre_order_traversal(1)

print("In-Order Traversal:")
newBT.in_order_traversal(1)

print("Post-Order Traversal:")
newBT.post_order_traversal(1)

print("Level-Order Traversal:")
newBT.level_order_traversal(1)

print(newBT.delete_node("Hot"))
print(newBT.search_node("Hot"))

print(newBT.delete_tree())
