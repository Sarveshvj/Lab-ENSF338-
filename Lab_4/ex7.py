import time
import matplotlib.pyplot as plt

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def insert_tail(self, node):
        if self.head is None:
            self.head = node
            return

        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = node

    def get_size(self):
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.next
        return count

    def get_element_at_pos(self, pos):
        curr = self.head
        for _ in range(pos):
            curr = curr.next
        return curr


    # ORIGINAL METHOD (O(n^2))
    def reverse_original(self):

        newhead = None
        prevNode = None

        for i in range(self.get_size()-1, -1, -1):

            currNode = self.get_element_at_pos(i)
            currNewNode = Node(currNode.data)

            if newhead is None:
                newhead = currNewNode
                prevNode = currNewNode
            else:
                prevNode.next = currNewNode
                prevNode = currNewNode

        self.head = newhead


    # OPTIMIZED METHOD (O(n))
    def reverse_optimized(self):

        prev = None
        curr = self.head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        self.head = prev


def create_list(n):

    lst = LinkedList()
    for i in range(n):
        lst.insert_tail(Node(i))
    return lst


sizes = [1000, 2000, 3000, 4000]

original_times = []
optimized_times = []

for size in sizes:

    total_time = 0
    for _ in range(100):
        lst = create_list(size)

        start = time.perf_counter()
        lst.reverse_original()
        end = time.perf_counter()

        total_time += end - start

    original_times.append(total_time / 100)


for size in sizes:

    total_time = 0
    for _ in range(100):
        lst = create_list(size)

        start = time.perf_counter()
        lst.reverse_optimized()
        end = time.perf_counter()

        total_time += end - start

    optimized_times.append(total_time / 100)


plt.plot(sizes, original_times, marker='o', label="Original O(n^2)")
plt.plot(sizes, optimized_times, marker='o', label="Optimized O(n)")

plt.xlabel("List Size")
plt.ylabel("Average Time (seconds)")
plt.title("Reverse Linked List Performance")
plt.legend()
plt.savefig('Graph-ex7')
plt.show()