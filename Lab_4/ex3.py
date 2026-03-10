# Exercise 3

# Q1: Strategy used to grow arrays when full

# Python lists are implemented as dynamic arrays in CPython.
# When the list becomes full, Python allocates a larger block
# of memory and copies the existing elements into it.

# In the CPython implementation (lists.c),
# inside the function list_resize(), the new capacity is
# calculated using an overallocation strategy:
#     new_allocated = newsize + (newsize >> 3) + 6
# For small lists (newsize < 9), it instead uses:
#     new_allocated = newsize + 3
# Since (newsize >> 3) is equivalent to newsize / 8,
# the list grows by approximately 12.5% plus a small constant.
# Therefore, the approximate growth factor is:
#     1.125  (12.5% growth)
# This strategy reduces the number of reallocations and ensures
# that append operations run in amortized O(1) time.

import sys
import time
import matplotlib.pyplot as plt

# Q2: Grow list from 0 to 63 elements and detect capacity change

lst = []
prev_size = sys.getsizeof(lst)

print("Capacity changes while growing list:")

for i in range(64):
    lst.append(i)
    current_size = sys.getsizeof(lst)

    if current_size != prev_size:
        overhead = sys.getsizeof([])
        pointer_size = 8
        capacity = (current_size - overhead) // pointer_size

        print(f"Length = {len(lst)}  -> capacity changed to {capacity}")
        prev_size = current_size

# Determine S (largest size that triggers expansion on append)

lst = []
prev_size = sys.getsizeof(lst)
S = 0

for i in range(100):
    lst.append(i)
    current_size = sys.getsizeof(lst)

    if current_size != prev_size:
        S = len(lst) - 1
        prev_size = current_size

print("\nLargest size S before expansion:", S)

# Q3: Measure time to grow from S to S+1 (causes resize)

times_resize = []

for _ in range(1000):
    lst = list(range(S))
    start = time.perf_counter()
    lst.append(0)
    end = time.perf_counter()
    times_resize.append(end - start)


# Q4: Measure time to grow from S-1 to S (no resize)
times_normal = []

for _ in range(1000):
    lst = list(range(S-1))
    start = time.perf_counter()
    lst.append(0)
    end = time.perf_counter()
    times_normal.append(end - start)

# Q5: Plot distributions

times_resize_us = [t * 1e6 for t in times_resize]
times_normal_us = [t * 1e6 for t in times_normal]

plt.hist(times_resize_us, bins=30, alpha=0.6, label="Resize (S → S+1)")
plt.hist(times_normal_us, bins=30, alpha=0.6, label="Normal (S-1 → S)")
plt.xlabel("Time (µs)")
plt.ylabel("Frequency")
plt.title("Append Time Distribution")
plt.legend()
plt.savefig('Graph-ex3')
plt.show()

# Q5 Discussion:
#
# The append operation that causes resizing (S → S+1) takes
# noticeably longer than the append that does not cause resizing
# (S-1 → S).
#
# This happens because when resizing occurs, Python must:
#
# 1. Allocate a new larger memory block
# 2. Copy all existing elements to the new memory
# 3. Free the old memory
#
# In contrast, when no resizing is required, the element is
# simply inserted into the already allocated space, which is
# much faster.
#
# This explains why most append operations are very fast,
# while occasional ones are slower. The overall average cost
# remains O(1) due to Python's overallocation strategy.