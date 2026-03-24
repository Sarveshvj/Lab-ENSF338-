import random

class Heap:
    def __init__(self):
        self.data = []
 
    def heapify(self, array):
        self.data = array[:]
        n = len(self.data)
        for i in range((n - 2) // 2, -1, -1):
            self._sift_down(i)
        return self.data
 
    def enqueue(self, value):
        self.data.append(value)
        self._sift_up(len(self.data) - 1)
 
    def dequeue(self):
        if len(self.data) == 0:
            return None
 
        root = self.data[0]
        last = self.data.pop()
 
        if len(self.data) > 0:
            self.data[0] = last
            self._sift_down(0)
 
        return root
 
    def _sift_up(self, index):
        parent = (index - 1) // 2
        while index > 0 and self.data[index] < self.data[parent]:
            self.data[index], self.data[parent] = self.data[parent], self.data[index]
            index = parent
            parent = (index - 1) // 2
 
    def _sift_down(self, index):
        n = len(self.data)
 
        while True:
            smallest = index
            left = 2 * index + 1
            right = 2 * index + 2
 
            if left < n and self.data[left] < self.data[smallest]:
                smallest = left
 
            if right < n and self.data[right] < self.data[smallest]:
                smallest = right
 
            if smallest == index:
                break
 
            self.data[index], self.data[smallest] = self.data[smallest], self.data[index]
            index = smallest

# Test 1: already a heap
h1 = Heap()
arr1 = [1, 3, 5, 7, 9]
expected1 = [1, 3, 5, 7, 9]
print("Test 1:", h1.heapify(arr1) == expected1)


# Test 2: empty array
h2 = Heap()
arr2 = []
expected2 = []
print("Test 2:", h2.heapify(arr2) == expected2)


# Test 3: random list (check heap property)
h3 = Heap()
arr3 = list(range(20))
random.shuffle(arr3)
heapified = h3.heapify(arr3)

def is_min_heap(arr):
    for i in range(len(arr)):
        left = 2*i + 1
        right = 2*i + 2
        if left < len(arr) and arr[i] > arr[left]:
            return False
        if right < len(arr) and arr[i] > arr[right]:
            return False
    return True

print("Test 3:", is_min_heap(heapified))
