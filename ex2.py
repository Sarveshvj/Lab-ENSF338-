import random
import time
import matplotlib.pyplot as plt

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def partition(arr, lb, hb):
    pivot_index = random.randint(lb, hb)
    arr[lb], arr[pivot_index] = arr[pivot_index], arr[lb]

    pivot = arr[lb]
    start = lb + 1
    end = hb

    while True:
        while start <= end and arr[start] <= pivot:
            start += 1

        while start <= end and arr[end] > pivot:
            end -= 1

        if start > end:
            break

        arr[start], arr[end] = arr[end], arr[start]

    arr[lb], arr[end] = arr[end], arr[lb]
    return end


def quickSort(arr, lb, hb):
    if lb < hb:
        pivot_index = partition(arr, lb, hb)
        quickSort(arr, lb, pivot_index - 1)
        quickSort(arr, pivot_index + 1, hb)
    return arr

def measure_time(sort_func, arr, repeats=5):
    total = 0
    for _ in range(repeats):
        temp = arr.copy()
        start = time.perf_counter()
        sort_func(temp)
        end = time.perf_counter()
        total += (end - start)
    return total / repeats

sizes = [10, 20, 30, 40, 50, 75, 100, 150, 200, 250,
         300, 400, 500, 600, 700, 800, 900, 1000, 1200, 1500]

bubble_best = []
bubble_worst = []
bubble_avg = []

quick_best = []
quick_worst = []
quick_avg = []

for n in sizes:

    sorted_arr = list(range(n))
    reverse_arr = list(range(n, 0, -1))
    random_arr = random.sample(range(n * 3), n)

    bubble_best.append(measure_time(bubbleSort, sorted_arr.copy()))
    bubble_worst.append(measure_time(bubbleSort, reverse_arr.copy()))
    bubble_avg.append(measure_time(bubbleSort, random_arr.copy()))

    quick_best.append(measure_time(lambda x: quickSort(x, 0, len(x) - 1), sorted_arr.copy()))
    quick_worst.append(measure_time(lambda x: quickSort(x, 0, len(x) - 1), reverse_arr.copy()))
    quick_avg.append(measure_time(lambda x: quickSort(x, 0, len(x) - 1), random_arr.copy()))

def plot_case(title, bubble_times, quick_times):
    plt.figure()
    plt.plot(sizes, bubble_times, label="Bubble Sort")
    plt.plot(sizes, quick_times, label="Quick Sort")

    for i in range(len(sizes)):
        if bubble_times[i] < quick_times[i]:
            plt.scatter(sizes[i], bubble_times[i])
        else:
            plt.scatter(sizes[i], quick_times[i])

    plt.xlabel("Input Size (n)")
    plt.ylabel("Time (seconds)")
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.savefig(f'{title}')
    plt.show()

plot_case("Best Case Performance", bubble_best, quick_best)
plot_case("Worst Case Performance", bubble_worst, quick_worst)
plot_case("Average Case Performance", bubble_avg, quick_avg)