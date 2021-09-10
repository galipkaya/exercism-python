class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        fmt = 'TreeNode(data={}, left={}, right={})'
        return fmt.format(self.data, self.left, self.right)


class BinarySearchTree:
    def __init__(self, tree_data):
        def add_item(node: TreeNode, data: str):
            if data <= node.data:
                if node.left is None:
                    node.left = TreeNode(data)
                else:
                    add_item(node.left, data)
            else:
                if node.right is None:
                    node.right = TreeNode(data)
                else:
                    add_item(node.right, data)

        self.root = TreeNode(tree_data[0])
        for i in range(1, len(tree_data)):
            add_item(self.root, tree_data[i])

    def data(self):
        return self.root

    def sorted_data(self):
        def _sorted_data(node: TreeNode):
            result = []
            if node.left is not None:
                result.extend(_sorted_data(node.left))
            result.append(node.data)
            if node.right is not None:
                result.extend(_sorted_data(node.right))
            return result

        return _sorted_data(self.root)
