import timeit
import random

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

def build_vector(elements):
    i = 1
    sorted_vector = []
    while i <= elements:
        sorted_vector.append(i)
        i += 1
    return sorted_vector

def shuffle_vector(vector):
    shuffled_vector = random.shuffle(vector)
    return shuffled_vector

def insert_vector(vector, root):
    i = 0
    while i < len(vector):
        root = insert(vector[i], root)
        i += 1
    return root
        
# **TEMP TESTING 
sorted_vector = build_vector(10)
print(sorted_vector)
shuffled_vector = shuffle_vector(sorted_vector.copy())
print(shuffled_vector)      # RETURNING NONE ?