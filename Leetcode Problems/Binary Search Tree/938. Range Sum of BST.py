class Solution:
    def rangeSumBST(self, root, low, high):
        self.ans = 0

        def search(node):
            if node:
                if low <= node.val <= high:
                    self.ans += node.val
                if low < node.val:
                    search(node.left)
                if node.val < high:
                    search(node.right)

        search(root)
        return self.ans
