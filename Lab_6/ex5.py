import random
import timeit
import heapq

# Part 1

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class ListPriorityQueue:
    def __init__(self):
        self.head = None

    def enqueue(self, value):
        new_node = Node(value)

        if self.head is None or value < self.head.value:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head

        while current.next is not None and current.next.value < value:
            current = current.next

        new_node.next = current.next
        current.next = new_node

    def dequeue(self):
        if self.head is None:
            return None

        value = self.head.value
        self.head = self.head.next
        return value


#Part 2

class HeapPriorityQueue:
    def __init__(self):
        self.heap = []

    def enqueue(self, value):
        heapq.heappush(self.heap, value)

    def dequeue(self):
        if len(self.heap) == 0:
            return None
        return heapq.heappop(self.heap)



#Part 3:

def generate_tasks(n):
    tasks = []

    for i in range(n):
        r = random.random()

        if r < 0.7:
            value = random.randint(1, 1000)
            tasks.append(("enqueue", value))
        else:
            tasks.append(("dequeue", None))

    return tasks


def run_tasks(queue, tasks):
    for task in tasks:
        if task[0] == "enqueue":
            queue.enqueue(task[1])
        else:
            queue.dequeue()


def test_list_queue(tasks):
    q = ListPriorityQueue()
    run_tasks(q, tasks)


def test_heap_queue(tasks):
    q = HeapPriorityQueue()
    run_tasks(q, tasks)


if __name__ == "__main__":
    random.seed(42)
    tasks = generate_tasks(1000)

    list_total_time = timeit.timeit(lambda: test_list_queue(tasks), number=1)
    heap_total_time = timeit.timeit(lambda: test_heap_queue(tasks), number=1)

    list_avg_time = list_total_time / len(tasks)
    heap_avg_time = heap_total_time / len(tasks)

    print("ListPriorityQueue total time:", list_total_time)
    print("ListPriorityQueue average time per task:", list_avg_time)

    print("HeapPriorityQueue total time:", heap_total_time)
    print("HeapPriorityQueue average time per task:", heap_avg_time)


# Part 4:

# HeapPriorityQueue is faster than ListPriorityQueue.
# From the experiment we can see the heap implementation takes less total time and less average time per task.
# This happens because heap operations are O(log n), while inserting into a sorted linked list takes O(n) since we must traverse the list to find the correct position.