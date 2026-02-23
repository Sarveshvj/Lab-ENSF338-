import time
import matplotlib.pyplot as plt
import sys
sys.setrecursionlimit(3000)

# Linear Search
def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

# Quicksort
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

def quickSort(arr, lb, hb):
    if lb < hb:
        pivot_index = partition(arr, lb, hb)
        quickSort(arr, lb, pivot_index - 1)
        quickSort(arr, pivot_index + 1, hb)

# Binary Search
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

sizes = [10, 20, 50, 100, 200, 500, 1000]

linear_times = []
quick_binary_times = []

for n in sizes:
    linear_total = 0
    quick_binary_total = 0

    for _ in range(100):
        arr = list(range(n))  
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
plt.plot(sizes, quick_binary_times, label="Quicksort + Binary Search (Worst Case)")

plt.xlabel("Input Size")
plt.ylabel("Average Time (seconds)")
plt.legend()
plt.title("Worst-Case Quicksort vs Linear Search")
plt.savefig("Worst Case")
plt.show()

"""
DISCUSSION:

In the worst-case scenario (already sorted array, pivot = first element):
- Quicksort performance degrades to O(n^2)
- Linear search remains O(n)
- Linear search can be faster than Quicksort + Binary Search even for moderately large arrays

Conclusion:
- Quicksort is highly sensitive to pivot choice
- Always consider input order or use randomized pivot to avoid worst-case
"""