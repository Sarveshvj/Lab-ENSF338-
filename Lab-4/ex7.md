## Q1:

Let n be the number of elements in the linked list.

The algorithm iterates through the list using the loop:

    for i in range(self.get_size()-1, -1, -1):

This loop runs n times.

Inside the loop, the method `get_element_at_pos(i)` is called. Since the list is implemented as a singly-linked list without a tail pointer, accessing an element at position `i` requires traversing the list from the head until that position is reached.

In the worst case, this traversal takes O(n) time.

Therefore:

* The loop runs n times
* Each iteration may take O(n) time due to `get_element_at_pos(i)`

Total time complexity:
T(n) = n × O(n) = O(n²)

Thus, the overall time complexity of the given `reverse()` implementation is O(n²).

## Q2:

The original implementation repeatedly traverses the list using 
get_element_at_pos(), which results in O(n²) time complexity.

The optimized version reverses the list by modifying the next 
pointers of each node while traversing the list once.

def reverse_optimized(self):
    prev = None
    curr = self.head

    while curr is not None:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    self.head = prev

This algorithm performs a single traversal of the list, so the time
complexity is O(n). This improves performance compared to the original
O(n²) implementation.
