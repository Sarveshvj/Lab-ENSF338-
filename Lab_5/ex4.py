import random
import timeit
import matplotlib.pyplot as plt

class ArrayQueue:
    def __init__(self):
        self.queue = []
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def enqueue(self, data):
        self.queue.insert(0, data)

    def dequeue(self):
        if self.isEmpty():
            return None
        
        return self.queue.pop()

    def __str__(self):
        return str(self.queue)
    
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head is None

    def enqueue(self, data):
        newNode = Node(data)

        if self.isEmpty():
            self.head = self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def dequeue(self):
        if self.isEmpty():
            return None

        if self.head == self.tail:
            data = self.tail.data
            self.head = self.tail = None
            return data

        current = self.head
        while current.next != self.tail:
            current = current.next

        data = self.tail.data
        current.next = None
        self.tail = current

        return data

    def __str__(self):
        current = self.head
        result = []
        while current:
            result.append(current.data)
            current = current.next
        return str(result)

def generate_tasks(n=10000):
    tasks = []

    for _ in range(n):
        if random.random() < 0.7:
            tasks.append(("enqueue", random.randint(1, 100)))
        else:
            tasks.append(("dequeue", None))

    return tasks

def run_tasks(queue, tasks):
    for task in tasks:
        if task[0] == "enqueue":
            queue.enqueue(task[1])
        else:
            queue.dequeue()


def measure_performance():
    array_times = []
    linked_times = []

    task_lists = [generate_tasks() for _ in range(100)]

    for tasks in task_lists:

        t1 = timeit.timeit(lambda: run_tasks(ArrayQueue(), tasks), number=1)
        array_times.append(t1)

        t2 = timeit.timeit(lambda: run_tasks(LinkedQueue(), tasks), number=1)
        linked_times.append(t2)

    print("Array Queue Times:", array_times)
    print("Linked Queue Times:", linked_times)

    return array_times, linked_times

def plot_results(array_times, linked_times):

    plt.hist(array_times, bins=20, alpha=0.5, label="Array Queue")
    plt.hist(linked_times, bins=20, alpha=0.5, label="Linked Queue")

    plt.xlabel("Execution Time")
    plt.ylabel("Frequency")
    plt.title("Queue Performance Comparison")

    plt.legend()
    plt.show()

if __name__ == "__main__":

    array_times, linked_times = measure_performance()

    print("Array Queue times:", array_times)
    print("Linked Queue times:", linked_times)

    plot_results(array_times, linked_times)


# Discussion:
# The experiment compares the performance of a queue implemented using a Python array
# and a singly linked list. In the array implementation, the enqueue operation uses
# insert(0), which requires shifting all elements and therefore has O(n) time complexity.
# The dequeue operation, however, uses pop() from the tail and runs in O(1) time.
#
# In the linked-list implementation, enqueue at the head takes O(1) time because it only
# updates pointers. However, dequeue requires traversing the list to find the node before
# the tail, making it O(n).
#
# Since the task lists contain 70% enqueue operations and 30% dequeue operations, the
# array implementation performs more expensive O(n) operations. As a result, the linked-
# list implementation generally performs slightly faster overall, which is reflected in
# the timing distributions shown in the plot.
