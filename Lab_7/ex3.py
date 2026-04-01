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


def _update_balances(node):
    if node is None:
        return

    _update_balances(node.left)
    _update_balances(node.right)
    node.balance = _height(node.right) - _height(node.left)


def _get_root(node):
    current = node
    while current.parent is not None:
        current = current.parent
    return current


def _left_rotate(root, node):
    new_root = node.right
    node.right = new_root.left

    if new_root.left is not None:
        new_root.left.parent = node

    new_root.parent = node.parent

    if node.parent is None:
        root = new_root
    else:
        if node.parent.left == node:
            node.parent.left = new_root
        else:
            node.parent.right = new_root

    new_root.left = node
    node.parent = new_root

    root = _get_root(new_root)
    _update_balances(root)
    return root


def _right_rotate(root, node):
    new_root = node.left
    node.left = new_root.right

    if new_root.right is not None:
        new_root.right.parent = node

    new_root.parent = node.parent

    if node.parent is None:
        root = new_root
    else:
        if node.parent.left == node:
            node.parent.left = new_root
        else:
            node.parent.right = new_root

    new_root.right = node
    node.parent = new_root

    root = _get_root(new_root)
    _update_balances(root)
    return root


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


def insert(data, root=None, show=True):
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
        if show:
            print("Case #1: Pivot not detected")
        return root

    elif data <= parent.data:
        parent.left = new_node
        new_node.parent = parent
    else:
        parent.right = new_node
        new_node.parent = parent

    pivot = new_node.parent
    while pivot is not None:
        if pivot.balance != 0:
            break
        pivot = pivot.parent

    if pivot is None:
        root = _get_root(new_node)
        _update_balances(root)
        if show:
            print("Case #1: Pivot not detected")
        return root

    old_balance = pivot.balance

    root = _get_root(new_node)
    _update_balances(root)

    if old_balance < 0 and data > pivot.data:
        if show:
            print("Case #2: A pivot exists, and a node was added to the shorter subtree")
        return root

    if old_balance > 0 and data <= pivot.data:
        if show:
            print("Case #2: A pivot exists, and a node was added to the shorter subtree")
        return root

    if old_balance < 0:
        child = pivot.left
        if child is not None and data <= child.data:
            if show:
                print("Case #3a: adding a node to an outside subtree")
            root = _right_rotate(root, pivot)
        else:
            if show:
                print("Case 3b not supported")

    elif old_balance > 0:
        child = pivot.right
        if child is not None and data > child.data:
            if show:
                print("Case #3a: adding a node to an outside subtree")
            root = _left_rotate(root, pivot)
        else:
            if show:
                print("Case 3b not supported")

    return root


def print_tree(node, indent=0, label="Root"):
    if node is None:
        return
    print(" " * indent + f"{label}: {node.data}  (bal={node.balance})")
    print_tree(node.left, indent + 4, "L")
    print_tree(node.right, indent + 4, "R")


if __name__ == "__main__":
    # Test 1
    print("=" * 50)
    print("Test 1 - Expected: Case #1")
    print("=" * 50)
    root1 = None
    root1 = insert(10, root1, True)
    print_tree(root1)
    print()

    # Test 2
    print("=" * 50)
    print("Test 2 - Expected: Case #2")
    print("=" * 50)
    root2 = None
    root2 = insert(10, root2, False)
    root2 = insert(5, root2, False)
    root2 = insert(15, root2, False)
    root2 = insert(3, root2, False)
    root2 = insert(8, root2, True)
    print_tree(root2)
    print()

    # Test 3
    print("=" * 50)
    print("Test 3 - Expected: Case #3a")
    print("=" * 50)
    root3 = None
    root3 = insert(10, root3, False)
    root3 = insert(5, root3, False)
    root3 = insert(3, root3, True)
    print_tree(root3)
    print()

    # Test 4
    print("=" * 50)
    print("Test 4 - Expected: Case #2")
    print("=" * 50)
    root4 = None
    root4 = insert(10, root4, False)
    root4 = insert(5, root4, False)
    root4 = insert(15, root4, True)
    print_tree(root4)
    print()

    # Test 5
    print("=" * 50)
    print("Test 5 - Expected: Case #3a")
    print("=" * 50)
    root5 = None
    root5 = insert(10, root5, False)
    root5 = insert(15, root5, False)
    root5 = insert(20, root5, True)
    print_tree(root5)
    print()

    # Test 6
    print("=" * 50)
    print("Test 6 - Expected: Case 3b not supported")
    print("=" * 50)
    root6 = None
    root6 = insert(10, root6, False)
    root6 = insert(5, root6, False)
    root6 = insert(8, root6, True)
    print_tree(root6)
    print()