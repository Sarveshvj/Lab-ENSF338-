import time 
import random 
import matplotlib.pyplot as plt


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linklist:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node


    def get_middle(self, start, end):
        slow = start
        fast = start 
        while fast != end and fast.next != end:
            fast = fast.next
            if fast != end:
                fast = fast.next 
                slow = slow.next 
        return slow
        
    def binary_search(self, target):
        start = self.head
        end = None

        while start != end:
            mid = self.get_middle(start, end)
            if mid.data == target:
                return True 
            elif mid.data < target:
                start = mid.next
            else:
                end = mid 
        return False

class Array:
    def __init__ (self,data):
        self.data = data
    def binary_search(self ,target):
        left = 0 
        right = len(self.data) - 1

        while left <= right:
            mid = (left + right) //2

            if self.data[mid] == target:
                return True
            elif self.data[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
    

'''
Binary search on an array has a time complexity of O(log n) because we can directly access the middle element, resulting in constant time complexity.
However, this is not the case with linked lists. We cannot directly access the middle element.
We must traverse the entire linked list to find it, which requires O(n) time complexity.
Although each traversal reduces the search space,
repeatedly searching for the middle element still results in a total time complexity of O(n).
Therefore, binary search on a linked list has a time complexity of O(n).
'''

def build_linklist(data):
    ll = linklist()
    for num in data:
        ll.append(num)
    return ll


sizes = [1000, 2000, 4000, 8000]
array_times = []
linklist_times = []

for size in sizes:
    data = list(range(size))

    arr = Array(data)
    ll = build_linklist(data)

    array_total = 0
    linklist_total = 0

    for i in range(100):
        target = random.choice(data)

        start = time.time()
        arr.binary_search(target)
        end = time.time()
        array_total += (end - start)

        start = time.time()
        ll.binary_search(target)
        end = time.time()
        linklist_total += (end - start)

    array_avg = array_total / 100
    linklist_avg = linklist_total / 100

    array_times.append(array_avg)
    linklist_times.append(linklist_avg)

    print("size =", size)
    print("array average time =", array_avg)
    print("linklist average time =", linklist_avg)


plt.plot(sizes, array_times, marker='o', label='Array Binary Search')
plt.plot(sizes, linklist_times, marker='o', label='Linked List Binary Search')

plt.plot(sizes, array_times, '--')
plt.plot(sizes, linklist_times, '--')

plt.xlabel("Input Size")
plt.ylabel("Average Time")
plt.title("Binary Search Performance")
plt.legend()
plt.grid(True)
plt.show()
