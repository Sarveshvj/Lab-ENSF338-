import random
import timeit


class PriorityQueueSort:
    def __init__(self):
        self.data = []

    def enqueue(self, value):
        self.data.append(value)
        self.data = self.merge_sort(self.data)

    def dequeue(self):
        if len(self.data) == 0:
            return None
        return self.data.pop(0)

    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])

        return self.merge(left, right)

    def merge(self, left, right):
        result = []
        i = 0
        j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])

        return result


class PriorityQueueInsert:
    def __init__(self):
        self.data = []

    def enqueue(self, value):
        i = 0
        while i < len(self.data) and self.data[i] < value:
            i += 1
        self.data.insert(i, value)

    def dequeue(self):
        if len(self.data) == 0:
            return None
        return self.data.pop(0)


def generate_tasks():
    tasks = []
    for _ in range(1000):
        if random.random() < 0.7:
            tasks.append(("enqueue", random.randint(1, 1000)))
        else:
            tasks.append(("dequeue", None))
    return tasks


def run_tasks(queue_class, tasks):
    q = queue_class()

    for task in tasks:
        if task[0] == "enqueue":
            q.enqueue(task[1])
        else:
            q.dequeue()


def measure():
    tasks_list = [generate_tasks() for _ in range(100)]

    times_sort = []
    times_insert = []

    for tasks in tasks_list:
        t1 = timeit.timeit(lambda: run_tasks(PriorityQueueSort, tasks), number=1)
        t2 = timeit.timeit(lambda: run_tasks(PriorityQueueInsert, tasks), number=1)

        times_sort.append(t1)
        times_insert.append(t2)

    avg_sort = sum(times_sort) / len(times_sort)
    avg_insert = sum(times_insert) / len(times_insert)

    print("Average time for PriorityQueueSort:", avg_sort)
    print("Average time for PriorityQueueInsert:", avg_insert)

    if avg_sort < avg_insert:
        print("PriorityQueueSort was faster in this test.")
    else:
        print("PriorityQueueInsert was faster in this test.")


if __name__ == "__main__":
    measure()


# Q5:
# In my tests, PriorityQueueInsert was faster.
# This makes sense because PriorityQueueSort sorts the whole list again every time enqueue a new value.
# PriorityQueueInsert still has to scan the list and insert the element, but that is usually less work than re-sorting the whole queue each time.