class Solution:
    def countUnivalSubtrees(self, root) -> int:
        self.count = 0

        def checkUni(node, parent):
            if not node:
                return True
            left = checkUni(node.left, node.val)
            right = checkUni(node.right, node.val)
            if left and right:
                self.count += 1
            return left and right and node.val == parent

        checkUni(root, None)
        return self.count
