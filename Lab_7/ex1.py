import random
import timeit
import matplotlib.pyplot as plt

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

def height(node):
    if node is None:
        return -1
    
    left_height = height(node.left)
    right_height = height(node.right)

    return max(left_height, right_height) + 1       # 1 return

def isBalanced(node):
    if node is None:
        return True
        
    left_height = height(node.left)
    right_height = height(node.right)

    balance = left_height - right_height

    if abs(balance) > 1:
        return False
    
    return isBalanced(node.left) and isBalanced(node.right)     # 1 return

# 3

def generate_thousand_tasks():
    # make list of 1000 integers
    int_list = list(range(1000))

    # make list of 1000 tasks (1000 shuffled lists)
    task_list = []
    for i in range(1000):
        task = int_list.copy()
        random.shuffle(task)
        task_list.append(task)

    return task_list        # 1 return

# 4

def largest_abs_balance(node):
    if node is None:
        return 0
    
    left_height = height(node.left)
    right_height = height(node.right)

    current_balance = abs(left_height - right_height)

    max_left = largest_abs_balance(node.left)
    max_right = largest_abs_balance(node.right)

    return max(current_balance, max_left, max_right)    # 1 return

def experiment(task_list):
    max_balances = []
    times = []

    for i, task in enumerate(task_list):
        root = None
        for data in task:
            root = insert(data, root)
        
        total_time = 0

        for data in task:
            start = timeit.default_timer()
            search(data, root)
            total_time += ( timeit.default_timer() - start )

        avg_time = total_time / len(task)

        max_balance = largest_abs_balance(root)

        max_balances.append(max_balance)
        times.append(avg_time)
    
    return max_balances, times

# 5

def plot_scatter(max_balances, times):
    plt.scatter(max_balances, times, alpha=0.3)
    plt.xlabel("Largest Absolute Balances")
    plt.ylabel("Search Time (s)")
    plt.title("Max BST Balance vs Search Performance")

    plt.show()

task_list = generate_thousand_tasks()
max_balances, times = experiment(task_list)
plot_scatter(max_balances, times)