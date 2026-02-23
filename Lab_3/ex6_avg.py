import random
import time
import matplotlib.pyplot as plt

# --- Linear Search ---
def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

# --- Quicksort ---
def partition(arr, lb, hb):
    pivot = arr[lb]
    i = lb + 1
    j = hb

    while True:
        while i <= j and arr[i] <= pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break

    arr[lb], arr[j] = arr[j], arr[lb]
    return j

def quickSort (arr, lb, hb):
    if lb < hb:
        pivot_index = partition(arr, lb, hb)
        quickSort(arr, lb, pivot_index - 1)
        quickSort(arr, pivot_index + 1, hb)
    return arr

# --- Binary Search ---
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# --- QS + BS combined ---
def quicksort_binary_search(arr, target):
    quickSort(arr, 0, len(arr) - 1)
    return binary_search(arr, target)

sizes = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]

linear_times = []
quick_binary_times = []

for n in sizes:
    linear_total = 0
    quick_binary_total = 0

    for _ in range(100):
        arr = list(range(n))
        random.shuffle(arr)
        target = n // 2

        # Linear Search timing
        start = time.perf_counter()
        linear_search(arr, target)
        end = time.perf_counter()
        linear_total += (end - start)

        # Quicksort + Binary Search timing
        arr_copy = arr.copy()
        start = time.perf_counter()
        quickSort(arr_copy, 0, len(arr_copy) - 1)
        binary_search(arr_copy, target)
        end = time.perf_counter()
        quick_binary_total += (end - start)

    linear_times.append(linear_total / 100)
    quick_binary_times.append(quick_binary_total / 100)

plt.plot(sizes, linear_times, label="Linear Search")
plt.plot(sizes, quick_binary_times, label="Quicksort + Binary Search")

plt.xlabel("Input Size")
plt.ylabel("Average Time (seconds)")
plt.legend()
plt.title("Average Case Performance")
plt.savefig("Average Case")
plt.show()

"""
DISCUSSION:

Linear search is faster for single searches on randomly shuffled arrays.

Reason:
- Linear search runs in O(n)
- Quicksort + binary search runs in O(n log n)
- Sorting overhead dominates when performing only one search

Conclusion:
- Linear search is better for one-time searches
- QS+Binary search only makes sense if searching multiple times on the same dataset
"""