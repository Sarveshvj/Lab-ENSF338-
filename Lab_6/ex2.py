import timeit
import random

# 1.

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
    shuffled_vector = vector.copy()
    random.shuffle(shuffled_vector)
    return shuffled_vector

def insert_vector(vector, root):
    i = 0
    while i < len(vector):
        root = insert(vector[i], root)
        i += 1
    return root

def binary_search(arr, key):
    lo = 0
    hi = (len(arr) - 1)
    while lo <= hi:
        mid = (lo + hi) // 2
        if key < arr[mid]:
            hi = mid - 1
        elif arr[mid] < key:
            lo = mid + 1
        else:
            return mid
    return -1

def bst_experiment():
    sorted_vector = build_vector(10000)
    shuffled_vector = shuffle_vector(sorted_vector)
    root = None
    root = insert_vector(shuffled_vector, root)

    total_time = 0
    
    for el in sorted_vector:
        def search_wrapper():
            return search(el, root)
        
        time = timeit.timeit(search_wrapper, number=10)
        total_time += time

    total_searches = len(sorted_vector) * 10
    average_time = total_time / total_searches

    return average_time, total_time

def bsa_experiment():
    sorted_vector = build_vector(10000)
    
    total_time = 0

    for el in sorted_vector:
        def search_wrapper():
            return binary_search(sorted_vector, el)
        
        time = timeit.timeit(search_wrapper, number=10)
        total_time += time

    total_searches = len(sorted_vector) * 10
    average_time = total_time / total_searches

    return average_time, total_time

average_time_1, total_time_1 = bst_experiment()
average_time_2, total_time_2 = bsa_experiment()

print(f"Average time 1: {average_time_1}")
print(f"Total time 1: {total_time_1}\n")
print(f"Average time 2: {average_time_2}")
print(f"Total time 2: {total_time_2}\n")

'''
4.
on a run, BST using a shuffled vector measured about 1.66 times faster than the array binary search by
total time, the BST also yielded faster a faster average time.
BST performing overall faster than the array binary search could likely be due to the BST experiment involving
a shuffled array, allowing for the best possible performance with a balanced tree or even due to the
binary search array implementation involving more complex operations, taking up more time than the BST implementation.
'''