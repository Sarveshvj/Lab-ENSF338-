import sys
import random
import matplotlib.pyplot as plt

sys.setrecursionlimit(20000)

def bubble_sort(arr):
    n = len(arr)
    swap_count = 0
    comp_count = 0

    for i in range(n):
        swap = False

        for j in range(0, n-i-1):
            comp_count += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap = True
                swap_count += 1
            
        if swap == False:
            break
    print(f"Sorted Array: {arr}")
    return comp_count, swap_count


def test_code():
    array1 = [64, 34, 25, 12, 22, 11, 90]
    comp_count, swap_count = bubble_sort(array1)
    print(f"comparisons: {comp_count}")
    print(f"swaps: {swap_count}")

def experiment(input_sizes):
    results_comp = []
    results_swap = []
    for n in input_sizes:
        arr = [random.randint(1, 1000) for x in range(n)]
        comp_count, swap_count = bubble_sort(arr)
        results_comp.append(comp_count)
        results_swap.append(swap_count)



    return results_comp, results_swap
    
def plot_results(input_sizes, results_comp, results_swap):
    form_comp = [n*(n-1)/2 for n in input_sizes]
    form_swap = [n*(n-1)/4 for n in input_sizes]

    plt.figure(1)
    plt.plot(input_sizes, results_comp, 'o-', label="Real Comps", markersize=8)
    plt.plot(input_sizes, form_comp, 'r--', label="Theoretical Comps")
    plt.xlabel("Input Size (n)")
    plt.ylabel("Num of Comparisons")
    plt.title("Comparisons vs Input Size")
    plt.legend()
    plt.grid(True)
    plt.xticks(input_sizes)

    plt.figure(2)
    plt.plot(input_sizes, results_swap, 'o-', label="Real Swaps", markersize=8)
    plt.plot(input_sizes, form_swap, 'r--', label="Theoretical avg. Swaps")
    plt.xlabel("Input Size (n)")
    plt.ylabel("Num of Swaps")
    plt.title("Swaps vs Input Size")
    plt.legend()
    plt.grid(True)
    plt.xticks(input_sizes)

    plt.show()

input_sizes = [10, 20, 30, 40, 50]
results_comp, results_swap = experiment(input_sizes)
plot_results(input_sizes, results_comp, results_swap)
