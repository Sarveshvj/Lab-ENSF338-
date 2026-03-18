import random
import timeit
import matplotlib.pyplot as plt
import numpy as np

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackArr:
    def __init__(self):
        self.stack = []
    
    def push(self, el):
        self.stack.append(el)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        return None

class StackList:
    def __init__(self):
        self.head = None

    def push(self, data):
        # add head of linked list, next node is previous head
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        # delete head of linked list, set next node as head
        if self.head is not None:
            self.head = self.head.next

def randTasks(num_of_tasks=10000, push_prob=0.7):
    # creates list of random tasks
    task_list = []
    for i in range(num_of_tasks):
        if random.random() < push_prob:
            task_list.append("push")
        else:
            task_list.append("pop")
    return task_list

def experiment(list_of_task_lists, num_lists=100):
    arr_times = []
    list_times = []

    for task_list in list_of_task_lists:
        # StackArr time
        stack_arr = StackArr()
        start = timeit.default_timer()
        for task in task_list:
            if task == "push":
                stack_arr.push(1)
            else:
                stack_arr.pop()
        end = timeit.default_timer()
        arr_times.append(end - start)

        # StackList time
        stack_list = StackList()
        start = timeit.default_timer()
        for task in task_list:
            if task == "push":
                stack_list.push(1)
            else:
                stack_list.pop()
        end = timeit.default_timer()
        list_times.append(end - start)
    
    return arr_times, list_times

list_of_task_lists = [randTasks() for i in range(100)]

arr_times, list_times = experiment(list_of_task_lists)

plt.figure(figsize=(10, 6))
plt.hist(arr_times, bins=30, alpha=0.5, label='Array Stack', color='blue')
plt.hist(list_times, bins=30, alpha=0.5, label='Linked List Stack', color='red')
plt.xlabel('Time (seconds)')
plt.ylabel('Frequency')
plt.title('Distribution of Execution Times')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# Array stack implementation generally has much faster execution times than the Linked List stack implementation
# Array stack implementation execution time frequency is the highest within the range 0.0009 - 0.0010 seconds
# Linked list stack implementation execution time frequency is highest within range  0.0015 - 0.0035 seconds