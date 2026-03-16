class Heap:
    def __init__(self):
        self.data = []
 
    def heapify(self, array):
        self.data = array[:]
        n = len(self.data)
        for i in range((n - 2) // 2, -1, -1):
            self._sift_down(i)
 
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


            