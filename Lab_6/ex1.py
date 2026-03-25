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

def sorted_experiment():
    sorted_vector = build_vector(10000)
    root = None
    root = insert_vector(sorted_vector, root)
    total_time = 0

    for el in sorted_vector:
        def search_wrapper():
            return search(el, root)
        time = timeit.timeit(search_wrapper, number=10)
        total_time += time

    total_searches = len(sorted_vector) * 10
    average_time = total_time / total_searches

    return average_time, total_time

# 3.

def shuffled_experiment():
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


# running experiments

average_time_1, total_time_1 = sorted_experiment()
average_time_2, total_time_2 = shuffled_experiment()

print(f"Average time 1: {average_time_1}")
print(f"Total time 1: {total_time_1}\n")
print(f"Average time 2: {average_time_2}")
print(f"Total time 2: {total_time_2}\n")

'''
4. 
on a run, shuffled_experiment() using a shuffled vector to build a tree by insertion measured about 257 times faster by total time
to search compared to sorted_experiment() which used the same vector but sorted, the shuffled vector also has a much faster
average time than the sorted vector.
The sorted vector produces a degenerate tree with every new element on the same side, while the shuffled
vector produces a balanced tree because of the varying input numbers, avoiding the worst case (degenerate tree)
and involving much less levels.
'''