import json
import time
import matplotlib.pyplot as plt


def binary_search(arr, target, first_mid):
    low = 0
    high = len(arr) - 1

    if first_mid < 0:
        first_mid = 0
    if first_mid > high:
        first_mid = high

    mid = first_mid

    if arr[mid] == target:
        return True
    elif arr[mid] < target:
        low = mid + 1
    else:
        high = mid - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return False


def measure_time(arr, target, mid):
    start = time.perf_counter()
    binary_search(arr, target, mid)
    end = time.perf_counter()
    return end - start


def main():
    data = json.load(open("ex7data.json"))
    tasks = json.load(open("ex7tasks.json"))

    n = len(data)
    results = []

    step = n // 100
    if step == 0:
        step = 1

    mids = list(range(0, n, step))

    for task in tasks:
        best_mid = None
        best_time = None

        for m in mids:
            t = measure_time(data, task, m)
            if best_time is None or t < best_time:
                best_time = t
                best_mid = m

        results.append((task, best_mid))

    x = [r[0] for r in results]
    y = [r[1] for r in results]

    plt.scatter(x, y)
    plt.xlabel("Search task")
    plt.ylabel("Best first midpoint")
    plt.title("Best first midpoint for each task")
    plt.show()

    print("Done")


if __name__ == "__main__":
    main()

    # Q4
#From the graph, the initial midpoint does affect performance a little.
#When the first midpoint is closer to the target value, the search reduces the range earlier, so it can finish slightly faster.
#However, binary search quickly halves the range anyway, so the overall difference is not very large.