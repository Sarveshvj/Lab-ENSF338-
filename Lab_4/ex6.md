# Exercise 6

## 1. Advantages and disadvantages of arrays vs linked lists
Arrays allow direct access to elements using an index, so accessing an element is O(1) times.  
They also work well with algorithms like binary search. However, inserting or deleting elements in the middle of an array can be expensive because many elements may need to be shifted, which takes O(n) time.

Linked lists are different because they do not support direct indexing. To access an element, we have to traverse the list from the beginning, which takes O(n) time. However, insertion and deletion can be easier. Once we know the correct position, we only need to update the pointers, which can take O(1) time.

So arrays are better when we need fast access, while linked lists are better when there are many insertions or deletions.

## 2. Replace function for arrays

A replace operation means changing the value of an element at a specific index.

Instead of deleting the element and inserting a new one, we can simply overwrite the value in the array: arr[i] = new_value. This operation takes O(1) time because no elements need to be shifted.

## 3. Sorting a doubly linked list
### Insertion sort
Insertion sort can be applied to a doubly linked list. We go through the list one node at a time and insert each element into the correct position in the sorted part of the list by updating the pointers.
### Merge sort
Merge sort is also suitable for doubly linked lists. The list can be divided into two halves, and then the sorted halves are merged together by reconnecting nodes.

---

## 4. Expected complexity

**Insertion sort**
- Array: O(n²)
- Doubly linked list: O(n²)

For arrays, inserting an element may require shifting many elements. For linked lists, we only update pointers, but we still need to search for the correct position.

**Merge sort**
- Array: O(n log n)
- Doubly linked list: O(n log n)

Merge sort works well for linked lists because merging can be done by changing pointers instead of copying elements.