import random
import timeit

# Binary search tree with insertion and search operations

class Node:
    def __init__(self, data, parent=None, left=None, right=None):
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right

def insert(data, root=None):
    current = root
    parent = None

    while current is not None:
        parent = current
        if data <= current.data:
            current = current.left
        else:
            current = current.right

    if root is None:
        root = Node(data)
    elif data <= parent.data:
        parent.left = Node(data, parent)
    else:
        parent.right = Node(data, parent)
        
    return root

def search(data, root):
    # efficient performed on "well-balanced" tree: O(logn)
    # less efficient if tree degenerated to linked list: O(n)
    current = root
    while current is not None:
        if data == current.data:
            return current
        elif data < current.data:
            current = current.left
        else:
            current = current.right
    return None

# 2

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data)
        inorder(root.right)

def height(node):
    if node is None:
        return -1
    
    left_height = height(node.left)
    right_height = height(node.right)

    return max(left_height, right_height) + 1

def isBalanced(node):
    if node is None:
        return True
        
    left_height = height(node.left)
    right_height = height(node.right)

    balance = left_height - right_height

    if abs(balance) > 1:
        return False
    
    return isBalanced(node.left) and isBalanced(node.right)

def generate_thousand_tasks():
    # make list of 1000 integers
    int_list = list(range(1000))

    # make list of 1000 tasks (1000 shuffled lists)
    task_list = []
    for i in range(1000):
        task = int_list.copy()
        random.shuffle(task)
        task_list.append(task)

    return task_list


