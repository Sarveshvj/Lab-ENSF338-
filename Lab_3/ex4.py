import time
import matplotlib.pyplot as plt
import sys
sys.setrecursionlimit(5000)

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

sizes = []
times = []

for n in range(100, 2000, 200):
    arr = list(range(n))  # sorted -> worst case
    start = time.time()
    quickSort(arr, 0, len(arr) - 1)
    end = time.time()

    sizes.append(n)
    times.append(end - start)


plt.plot(sizes, times, 'o-', label="Measured Time")

# Interpolating n^2 curve
n2 = [ (n**2)/1e7 for n in sizes ]
plt.plot(sizes, n2, '--', label="O(n^2) reference")

plt.xlabel("Input Size (n)")
plt.ylabel("Time (seconds)")
plt.title("QuickSort Worst-Case Complexity")
plt.legend()
plt.savefig("QuickSort Worst-Case")
plt.show()