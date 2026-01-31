import timeit
import random
import matplotlib.pyplot as plt

# Linear search function
def linear_search(arr, target):
    for x in arr:
        if x == target:
            return True
    return False

# Setup data
n = 1000
data = list(range(n))
target = random.choice(data)

def test_func():
    linear_search(data, target)

# Time using timeit.repeat
times = timeit.repeat(stmt=test_func, repeat=1000, number=1)

# Plot histogram
plt.figure()
plt.hist(times)
plt.xlabel("Processing Time (seconds)")
plt.ylabel("Frequency")
plt.title("Histogram of Linear Search Times (1000 Records)")
plt.savefig("output.3.3.png")
plt.show()
