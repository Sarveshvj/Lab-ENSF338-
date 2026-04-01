class Node:
    def __init__(self, data, parent=None, left=None, right=None):
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right
        self.balance = 0


def _height(node):
    if node is None:
        return -1
    return 1 + max(_height(node.left), _height(node.right))


def _update_balances_from(node):
    current = node
    while current is not None:
        current.balance = _height(current.right) - _height(current.left)
        current = current.parent


def search(data, root):
    current = root
    while current is not None:
        if data == current.data:
            return current
        elif data < current.data:
            current = current.left
        else:
            current = current.right
    return None


def insert(data, root=None):
    current = root
    parent = None

    while current is not None:
        parent = current
        if data <= current.data:
            current = current.left
        else:
            current = current.right

    new_node = Node(data)

    if root is None:
        root = new_node
    elif data <= parent.data:
        parent.left = new_node
        new_node.parent = parent
    else:
        parent.right = new_node
        new_node.parent = parent

    pivot = None
    ancestor = new_node.parent
    while ancestor is not None:
        if abs(ancestor.balance) == 1:
            pivot = ancestor
            break
        ancestor = ancestor.parent

    _update_balances_from(new_node)

    if pivot is None:
        print("Case #1: Pivot not detected")

    elif abs(pivot.balance) <= 1:
        print("Case #2: A pivot exists, and a node was added to the shorter subtree")

    else:
        print("Case 3 not supported")

    return root

def print_tree(node, indent=0, label="Root"):
    if node is None:
        return
    print(" " * indent + f"{label}: {node.data}  (bal={node.balance})")
    print_tree(node.left,  indent + 4, "L")
    print_tree(node.right, indent + 4, "R")


if __name__ == "__main__":
    # Test 1
    print("=" * 50)
    print("Test 1 - Expected: Case #1 (first node, no pivot)")
    print("=" * 50)
    root1 = None
    print("  Inserting 10:")
    root1 = insert(10, root1)
    print_tree(root1)
    print()

    # Test 2
    print("=" * 50)
    print("Test 2 - Expected: Case #1 for all insertions (no pivot)")
    print("=" * 50)
    root2 = None
    for val in [10, 5, 15]:
        print(f"  Inserting {val}:")
        root2 = insert(val, root2)
    print_tree(root2)
    print()

    # Test 3
    print("=" * 50)
    print("Test 3 - Expected: Case #2 (pivot at node 5, shorter subtree)")
    print("=" * 50)
    root3 = None
    for val in [10, 5, 15, 3]:
        root3 = insert(val, root3)   # silent setup
    print("  Inserting 8 (triggers Case 2):")
    root3 = insert(8, root3)
    print_tree(root3)
    print()

    # Test 4
    print("=" * 50)
    print("Test 4 - Expected: Case 3 not supported (left-left imbalance)")
    print("=" * 50)
    root4 = None
    for val in [10, 5]:
        root4 = insert(val, root4)
    print("  Inserting 3 (triggers Case 3):")
    root4 = insert(3, root4)
    print_tree(root4)
    print()
