import random
import timeit
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit



def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1



def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1



sizes = [1000, 2000, 4000, 8000, 16000, 32000]

linear_times = []
binary_times = []


for n in sizes:
    arr = list(range(n))

    total_linear = 0
    total_binary = 0

    for _ in range(1000):
        target = random.choice(arr)

        t1 = timeit.timeit(
            lambda: linear_search(arr, target),
            number=100
        )

        t2 = timeit.timeit(
            lambda: binary_search(arr, target),
            number=100
        )

        total_linear += t1
        total_binary += t2

    linear_times.append(total_linear / 1000)
    binary_times.append(total_binary / 1000)



def linear_func(x, a, b):
    return a * x + b


def log_func(x, a, b):
    return a * np.log2(x) + b


sizes_np = np.array(sizes)

popt_linear, _ = curve_fit(linear_func, sizes_np, linear_times)
popt_binary, _ = curve_fit(log_func, sizes_np, binary_times)


plt.scatter(sizes, linear_times, label="linear search")
plt.plot(sizes, linear_func(sizes_np, *popt_linear), "--")

plt.scatter(sizes, binary_times, label="binary search")
plt.plot(sizes, log_func(sizes_np, *popt_binary), "--")

plt.xlabel("n")
plt.ylabel("time (seconds)")
plt.title("Linear vs Binary search timing")
plt.legend()
plt.grid(True)
plt.show()


"""
4:

For linear search, the data fits well to the linear function (a*n + b).
As n increases, the running time grows at roughly the same rate.
This is expected, as linear search might require checking many elements.
For binary search, the data fits better to the log2(n) function.
The running time grows much more slowly compared to linear search.
This is reasonable, as the search range is halved with each step.
Due to timing noise, the measurements are not perfectly smooth, butthe overall trend is consistent with what we learned in class about O(n) and O(log n).
"""
