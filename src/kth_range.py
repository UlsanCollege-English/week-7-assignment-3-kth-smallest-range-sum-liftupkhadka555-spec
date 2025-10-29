class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    """Insert key into BST, reject duplicates, and return new root."""
    if root is None:
        return Node(key)
    
    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    # If key == root.key: do nothing (reject duplicates)
    return root

def kth_smallest(root, k):
    """Return the k-th smallest element in BST. Raise IndexError if k is invalid."""
    stack = []
    node = root
    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        k -= 1
        if k == 0:
            return node.key
        node = node.right
    # If k is still not 0, it's out of bounds
    raise IndexError("k is out of bounds")

def range_sum_bst(root, low, high):
    """Return sum of all keys in BST within [low, high]."""
    if root is None:
        return 0
    total = 0
    if low <= root.key <= high:
        total += root.key
    if root.key > low:
        total += range_sum_bst(root.left, low, high)
    if root.key < high:
        total += range_sum_bst(root.right, low, high)
    return total

# Helper function to build BST from list (useful for tests)
def build(lst):
    root = None
    for key in lst:
        root = insert(root, key)
    return root

# Example usage
if __name__ == "__main__":
    values = [10, 5, 15, 3, 7, 18]
    root = build(values)

    print("3rd smallest:", kth_smallest(root, 3))  # Output: 7
    print("Range sum 7-15:", range_sum_bst(root, 7, 15))  # Output: 32
