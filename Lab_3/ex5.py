import sys
import random
import matplotlib.pyplot as plt
import timeit

sys.setrecursionlimit(20000)

def binary_search(arr, key, start, end):
    if start == end:
        if arr[start] > key:
            return start
        else:
            return start+1
    if start > end:
        return start
    
    mid = (start+end)//2
    if arr[mid] < key:
        return binary_search(arr, key, mid+1, end)
    elif arr[mid] > key:
        return binary_search(arr, key, start, mid-1)
    else:
        return mid
    
def binary_insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = binary_search(arr, key, 0, i-1)
        temp = key
        for k in range(i, j, -1):
            arr[k] = arr[k-1]
        arr[j] = temp
    return arr

def trad_insert_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def experiment(input_sizes):
    trad_times = []
    bina_times = []
    for n in input_sizes:
        arr = [random.randint(1, 1000) for x in range(n)]
        trad_time = timeit.timeit(lambda: trad_insert_sort(arr.copy()), number=100)
        bina_time = timeit.timeit(lambda: binary_insertion_sort(arr.copy()), number=100)
        trad_times.append(trad_time)
        bina_times.append(bina_time)

    return trad_times, bina_times

def plot_results(input_sizes, trad_times, bina_times):

    plt.figure(1)
    plt.plot(input_sizes, trad_times, 'bo-', label="Tradition Sort", markersize=8)
    plt.plot(input_sizes, bina_times, 'go-', label="Binary Sort")
    plt.xlabel("Input Size (n)")
    plt.ylabel("Time")
    plt.title("Insertion Sort Times: Traditional vs Binary")
    plt.legend()
    plt.grid(True)
    plt.xticks(input_sizes)
    plt.show()

input_sizes = [10, 20, 30, 40, 50, 100, 200, 300]

trad_times, bina_times = experiment(input_sizes)
plot_results(input_sizes, trad_times, bina_times)

'''
Binary sort algorithm is faster. At lower input sizes, the two are comparably similar until 
about n >= 100, in which binary has noticeably lower times than traditional sorting.
'''