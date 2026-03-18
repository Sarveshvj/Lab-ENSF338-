class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class ArrCircularQueue:
    def __init__(self, cap):
        self.cap = cap
        self.arr = [0] * cap
        self.front = 0
        self.size = 0
    
    def enqueue(self, element):
        # adds item to back of queue
        if self.size == self.cap:
            print("enqueue None")
            return
        back = (self.front + self.size) % self.cap
        self.arr[back] = element
        self.size += 1
        print(f"enqueue {element}")

    def dequeue(self):
        # removes and returns front-most item in queue
        if self.size == 0:
            print("dequeue None")
            return -1
        front_item = self.arr[self.front]
        self.front = (self.front + 1) % self.cap
        self.size -= 1
        print(f"dequeue {front_item}")
        return front_item
    
    def peek(self):
        # returns front most element
        if self.size == 0:
            print("peek None")
            return -1
        print(f"peek {self.arr[self.front]}")
        return self.arr[self.front]
    
class LinkedListQueue:
    def __init__(self, cap=None):
        self.cap = cap
        self.front = self.back = None
        self.size = 0
    
    def enqueue(self, item):
        if self.cap is not None and self.size == self.cap:
            print("enqueue None")
            return

        newNode = Node(item)

        if self.front is None:
            self.front = newNode
        else:
            self.back.next = newNode
        
        self.back = newNode
        self.back.next = self.front
        self.size += 1
        print(f"enqueue {item}")

    def dequeue(self):
        if self.front is None:
            print("dequeue None")
            return -1
        
        value = None

        if self.front == self.back:
            value = self.front.data
            self.front = self.back = None
        else:
            temp = self.front
            value = temp.data
            self.front = self.front.next
            self.back.next = self.front
        
        self.size -= 1
        print(f"dequeue {value}")
        return value
    
    def peek(self):
        front = self.front

        if front is None:
            print("peek None")
            return -1
        print(f"peek {front.data}")
        return front.data
    
Mylist = LinkedListQueue(3)

Mylist.peek()
Mylist.dequeue()
Mylist.dequeue()
Mylist.peek()
Mylist.dequeue()

Mylist.enqueue(5)
Mylist.enqueue(10)
Mylist.peek()
Mylist.enqueue(15)
Mylist.enqueue(20)

Mylist.peek()
Mylist.dequeue()
Mylist.enqueue(20)
Mylist.enqueue(25)
Mylist.peek()

Mylist.dequeue()
Mylist.dequeue()
Mylist.peek()
Mylist.enqueue(25)
Mylist.enqueue(30)

Mylist.dequeue()
Mylist.peek()
Mylist.dequeue()
Mylist.dequeue()
Mylist.peek()

Mylist.dequeue()
Mylist.enqueue(35)
Mylist.enqueue(40)
Mylist.peek()
Mylist.dequeue()

Mylist.enqueue(45)
Mylist.enqueue(50)
Mylist.dequeue()
Mylist.enqueue(55)
Mylist.enqueue(60)

Mylist.peek()
Mylist.dequeue()
Mylist.dequeue()
Mylist.dequeue()
Mylist.peek()