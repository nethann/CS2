class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def tree_height(node):
    if not node:
        return -1
    return 1 + max(tree_height(node.left), tree_height(node.right))

def count_leaf_nodes(node):
    if not node:
        return 0
    if not node.left and not node.right:
        return 1
    return count_leaf_nodes(node.left) + count_leaf_nodes(node.right)

def is_bst(node, min_val=float('-inf'), max_val=float('inf')):
    if not node:
        return True
    if not (min_val < node.value < max_val):
        return False
    return is_bst(node.left, min_val, node.value) and is_bst(node.right, node.value, max_val)

def is_balanced(node):
    def check_balance(node):
        if not node:
            return 0, True
        left_height, left_balanced = check_balance(node.left)
        right_height, right_balanced = check_balance(node.right)
        balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1
        return 1 + max(left_height, right_height), balanced

    _, balanced = check_balance(node)
    return balanced

def tree_info(node):
    print(f"Height of the tree: {tree_height(node)}")
    print(f"Number of leaf nodes: {count_leaf_nodes(node)}")
    print(f"Is a Binary Search Tree: {'Yes' if is_bst(node) else 'No'}")
    print(f"Is Balanced: {'Yes' if is_balanced(node) else 'No'}")

# Example usage
root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
tree_info(root)


