class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_valid_bst(root):

    def validate(node, low, high):

        if not node:
            return True

        if node.val <= low or node.val >= high:
            return False

        return validate(node.left, low, node.val) and validate(node.right, node.val, high)

    return validate(root, float('-inf'), float('inf'))

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

print(is_valid_bst(root))
