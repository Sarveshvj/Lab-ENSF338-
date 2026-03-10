import timeit
import random
import matplotlib.pyplot as plt

# INEFFICIENT IMPLEMENTATION (Bubble sort)

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr

# Worst Case Complexity: O(n^2)

# EFFICIENT IMPLEMENTATION (Merge sort)
def mergeSort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        mid = (low + high) // 2
        mergeSort(arr, low, mid)
        mergeSort(arr, mid+1, high)
        merge(arr, low, mid, high)
    return arr

def merge(arr, low, mid, high):
    n1 = mid - low + 1
    n2 = high - mid

    L = [0] * n1
    R = [0] * n2

    for i in range(n1):
        L[i] = arr[low + i]
    for j in range(n2):
        R[j] = arr[mid + 1 + j]
        
    i = 0  
    j = 0  
    k = low  

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

# Worst Case Complexity: O(nlogn)

def experiment(input_size, measurements):

    bubble_list = []
    merge_list = []

    for i in range(measurements):
        arr1 = [random.randint(1, 1000) for n in range(input_size)]
        bubble_time = timeit.timeit(lambda: bubbleSort(arr1), number = 1) * 1000 # in ms
        bubble_list.append(bubble_time)
        arr2 = [random.randint(1, 1000) for n in range(input_size)]
        merge_time = timeit.timeit(lambda: mergeSort(arr2), number = 1) * 1000 # in ms
        merge_list.append(merge_time)
        
    return bubble_list, merge_list, input_size

def plot_results(bubble_list, merge_list, input_size):
    
    plt.figure(figsize=(10, 6))
    
    plt.hist(bubble_list, bins=20, alpha=0.7, color='red', edgecolor='black', 
             label=f'Bubble Sort')
    plt.hist(merge_list, bins=20, alpha=0.7, color='green', edgecolor='black',
             label=f'Merge Sort')
    
    plt.xlabel('Time (milliseconds)')
    plt.ylabel('Frequency')
    plt.title(f'bubbleSort vs mergeSort times (n={input_size}, {len(bubble_list)} measurements)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.show()



bubble_list, merge_list, input_size = experiment(1000, 100)
plot_results(bubble_list, merge_list, input_size)
