class TreeNode:
    def __init__(self, value, left=None, right=None):
        #Initializes tree node with a value and optional left and right children.
        self.value = value
        self.left = left
        self.right = right

def tree_height(node):
    #Calculates the height of the binary tree.
    if not node:
        return -1
    return 1 + max(tree_height(node.left), tree_height(node.right))

def count_leaf_nodes(node):
    #Counts number of leaf nodes in the binary tree.
    if not node:
        return 0
    if not node.left and not node.right:
        return 1
    return count_leaf_nodes(node.left) + count_leaf_nodes(node.right)

def is_bst(node, min_val=float('-inf'), max_val=float('inf')):
    #Checks if binary tree is a Binary Search Tree.
    if not node:
        return True
    if not (min_val < node.value < max_val):
        return False
    return is_bst(node.left, min_val, node.value) and is_bst(node.right, node.value, max_val)

def is_balanced(node):
    #checks if the binary tree is balanced
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
    #printing the information
    print(f"Height of the tree: {tree_height(node)}")
    print(f"Number of leaf nodes: {count_leaf_nodes(node)}")
    print(f"Is a Binary Search Tree: {'Yes' if is_bst(node) else 'No'}")
    print(f"Is Balanced: {'Yes' if is_balanced(node) else 'No'}")

# Example usage
root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
tree_info(root)


